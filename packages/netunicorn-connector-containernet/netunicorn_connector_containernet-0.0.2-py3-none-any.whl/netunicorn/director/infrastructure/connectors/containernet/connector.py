from __future__ import annotations

import asyncio
import json
import logging
import os
import random
import string
from logging import Logger
from typing import Optional, Tuple, Any

import docker
import docker.errors

import yaml
from netunicorn.base import Architecture, DockerImage, Result, Failure, Success, is_successful
from netunicorn.base.deployment import Deployment
from netunicorn.base.nodes import Node, Nodes, UncountableNodePool

from netunicorn.director.base.connectors.protocol import (
    NetunicornConnectorProtocol,
)
from netunicorn.director.base.connectors.types import StopExecutorRequest

HEADER = [
    "#!/usr/bin/python3",
    "import time",
    "from mininet.net import Containernet",
    "from mininet.node import Controller",
    "from mininet.link import TCLink",
    "from mininet.log import setLogLevel",
    "setLogLevel('debug')",
    "net = Containernet(controller=Controller)",
    "net.addController('c0')",
]

FOOTER = [
    "net.start()",
    "[d.cmd('kill -SIGUSR1 1') for d in netunicorn_containernet_node_list]",
    "while any(x._is_container_running() for x in netunicorn_containernet_node_list): time.sleep(1)",
    "net.stop()",
]


class ContainernetConnector(NetunicornConnectorProtocol):
    def __init__(
            self,
            connector_name: str,
            configuration: str | None,
            netunicorn_gateway: str,
            logger: Optional[Logger] = None,
    ):
        self.connector_name = connector_name
        self.configuration = configuration

        # initialize is guaranteed to be called before any other method or we raise exceptions anyway
        self.client: docker.DockerClient
        self.architecture: Architecture

        if self.configuration is None:
            self.docker_endpoint = 'unix://var/run/docker.sock'
            self.working_folder = "/tmp"
        else:
            with open(self.configuration, 'r') as f:
                config = yaml.safe_load(f)
            self.docker_endpoint = config['netunicorn.containernet.docker.docker_endpoint']
            self.working_folder = config.get('netunicorn.containernet.working_folder', "/tmp")

        self.netunicorn_gateway = netunicorn_gateway

        self.logger = logger
        if logger is None:
            logging.basicConfig(level=logging.DEBUG)
            self.logger = logging.getLogger(__name__)

        self._init_client()
        self.experiment_containers: dict[str, list[str]] = {}  # optional (to still be stateless) to help stopping containers

    def _init_client(self):
        self.client = docker.DockerClient(base_url=self.docker_endpoint)
        version = self.client.version()
        assert version['Os'] == 'linux'
        self.architecture = Architecture.UNKNOWN
        if version['Arch'] == 'amd64':
            self.architecture = Architecture.LINUX_AMD64
        elif version['Arch'] == 'aarch64':
            self.architecture = Architecture.LINUX_ARM64
        else:
            self.logger.warning(f"Unknown architecture: {version['Arch']}")


    async def initialize(self, *args: Any, **kwargs: Any) -> None:
        if 'docker_endpoint' in kwargs:
            self.docker_endpoint = kwargs['docker_endpoint']
        if 'working_folder' in kwargs:
            self.working_folder = kwargs['working_folder']
        if 'netunicorn_gateway' in kwargs:
            self.netunicorn_gateway = kwargs['netunicorn_gateway']
        if not self.netunicorn_gateway:
            raise ValueError("netunicorn_gateway must be set during either __init__ or initialize")

        self._init_client()
        if not os.path.exists(self.working_folder):
            os.makedirs(self.working_folder)

        self.logger.info("Initialized Containernet connector")

    async def health(self, *args: Any, **kwargs: Any) -> Tuple[bool, str]:
        try:
            self.client.ping()
            self.logger.debug('ContainernetConnector is healthy')
            return True, 'OK'
        except Exception as e:
            self.logger.exception(e)
            return False, str(e)

    async def shutdown(self, *args: Any, **kwargs: Any) -> None:
        pass

    async def get_nodes(
            self,
            username: str,
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> Nodes:
        return UncountableNodePool(
            node_template=[
                Node(
                    name=f"node",
                    properties={"netunicorn-environments": {"DockerImage"}},
                    architecture=self.architecture,
                ),
            ]
        )

    @staticmethod
    def _normalize_name(name: str) -> Result[str, str]:
        """check that the name is the valid Python identifier"""
        if not name.isidentifier():
            return Failure(
                f"WARNING: name {name} is not a valid Python identifier."
                f" Please, use alphanumeric characters only"
            )
        return Success("")

    def _default_network_definition(self, deployments: list[Deployment]) -> str:
        self.logger.debug("Creating default network definition")
        return json.dumps([
            "default_switch = net.addSwitch('s0')",
            *(f"net.addLink({d.node.name}, default_switch)" for d in deployments)
        ])

    def _get_topology_filename(self, experiment_id: str) -> str:
        return os.path.join(self.working_folder, f"{experiment_id}_topology.py")

    @staticmethod
    def _get_containernet_container_name(experiment_id: str) -> str:
        return f"containernet.{experiment_id}"

    def _get_nodes_definition(self, experiment_id: str, deployments: list[Deployment]) -> list[str]:
        lines = []

        for deployment in deployments:
            deployment.environment_definition.runtime_context.environment_variables.update(
                {
                    'NETUNICORN_GATEWAY_ENDPOINT': self.netunicorn_gateway,
                    'NETUNICORN_EXECUTOR_ID': deployment.executor_id,
                    'NETUNICORN_EXPERIMENT_ID': experiment_id,
                }
            )

            # to use instead of deployment.node.name for container name
            # reason: mininet creates a virtual interface using `ip link add name <name>-eth0 ...`,
            # and the total name of ip link should be less than 16 symbols, so without `-eth99` we have 9 symbols
            # let's use 8 just in case
            random_node_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
            if experiment_id in self.experiment_containers:
                self.experiment_containers[experiment_id].append(f"mn.{random_node_name}")
            self.logger.debug(f"Added container {random_node_name} to experiment {experiment_id}")

            line = ''.join((
                f"{deployment.node.name} = net.addDocker(",
                f"'{random_node_name}',",
                f"dimage='{deployment.environment_definition.image}',",
                f"environment={deployment.environment_definition.runtime_context.environment_variables},",
                f"port_bindings={deployment.environment_definition.runtime_context.ports_mapping},",
                f"ports={list(deployment.environment_definition.runtime_context.ports_mapping.keys())},",
                f"ip='{deployment.node.properties['ip']}'," if 'ip' in deployment.node.properties else '',
                """dcmd=["bash", "-c", "echo Waiting for ContainerNet to start experiment...; trap 'sigusr1_received=true' SIGUSR1; while [[ -z $sigusr1_received ]]; do sleep 1; done; python3 -m netunicorn.executor"]""",
                ")"
            ))

            lines.append(line)

        lines.append(
            f"netunicorn_containernet_node_list = [{', '.join(d.node.name for d in deployments)}]"
        )

        return lines

    async def _create_containernet_topology(
            self,
            experiment_id: str,
            deployments: list[Deployment],
            deployment_context: Optional[dict[str, str]],
    ) -> Result[None, str]:
        # get network definition
        deployment_context = deployment_context or {}
        network_definition_serialized = deployment_context.get("network_definition", self._default_network_definition(deployments))
        try:
            network_definition = json.loads(network_definition_serialized)
        except (json.JSONDecodeError, ValueError) as e:
            return Failure(f"Invalid network definition: {e}")

        # simple verification, cannot do anything beyond that
        if not (isinstance(network_definition, list) and all(isinstance(x, str) for x in network_definition)):
            return Failure(f"Invalid network definition: should be a list of strings, received {network_definition}")

        topology_script = (
            *HEADER,
            *self._get_nodes_definition(experiment_id, deployments),
            *network_definition,
            *FOOTER,
        )
        topology_script = '\n'.join(topology_script)

        topology_filename = self._get_topology_filename(experiment_id)
        with open(topology_filename, "w") as f:
            f.write(topology_script)

        return Success(None)

    async def deploy(
            self,
            username: str,
            experiment_id: str,
            deployments: list[Deployment],
            deployment_context: Optional[dict[str, str]],
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> dict[str, Result[Optional[str], str]]:
        """
        Input data:
        - deployments: each deployment is a node (container) to be deployed.
        Each deployment should be a unique node (with unique name), because we cannot deploy multiple containers to the same "host"

        - deployment_context: can contain key "network-definition" with JSON-serialized list of strings as a value.
        Each string is a valid Python code with mininet commands to be executed before the deployment.
        The point here is to give the user the full control over the network topology with usual Mininet syntax
        and somehow serialize it and pass to the Containernet. Super secure, but I'm not sure what are better variants here
        as anyway user works with Containernet container that is privileged.

        Important info:
        - Containernet container name: `containernet.{experiment_id}`
        - All subsequent containers have names: `mn.containernet.{experiment_id}.{deployment.node.name}`

        """
        self.experiment_containers[experiment_id] = []
        result: dict[str, Result[str, str]] = {}
        node_names = set()
        for deployment in deployments:
            # check names
            if not deployment.node.name.isidentifier():
                result[deployment.executor_id] = Failure(
                    f"WARNING: name {deployment.node.name} is not a valid Python identifier."
                    f" Please, use alphanumeric characters only"
                )
                continue

            # all nodes should be unique
            if deployment.node.name in node_names:
                result[deployment.executor_id] = Failure(
                    f"WARNING: node name {deployment.node.name} is not unique. All node names should be unique."
                )
                continue
            node_names.add(deployment.node.name)

            # check if environment is DockerImage
            if not isinstance(deployment.environment_definition, DockerImage):
                result[deployment.executor_id] = Failure(
                    f"Supports only docker images, but received {deployment.environment_definition}"
                )
        deployments = [d for d in deployments if d.executor_id not in result]

        # create custom containernet topology
        topology_result = await self._create_containernet_topology(
            experiment_id,
            deployments,
            deployment_context,
        )
        if not is_successful(topology_result):
            self.logger.debug(f"Topology creation failed: {topology_result}")
            return result | {d.executor_id: topology_result for d in deployments}

        # at this point we checked that nodes are valid and created a topology file

        for deployment in deployments:
            try:
                self.client.images.pull(deployment.environment_definition.image)
                self.logger.debug(f"Image {deployment.environment_definition.image} pulled")
                result[deployment.executor_id] = Success(None)
            except docker.errors.ImageNotFound as e:
                result[deployment.executor_id] = Failure(e)
        return result

    async def execute(
            self,
            username: str,
            experiment_id: str,
            deployments: list[Deployment],
            execution_context: Optional[dict[str, str]],
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> dict[str, Result[Optional[str], str]]:

        # docker run --name containernet -it --rm --privileged --pid='host'
        # -v /var/run/docker.sock:/var/run/docker.sock
        # -v /tmp/<custom_topology_file>:/custom_topology.py
        # netunicorn/containernet python3 /custom_topology.py

        containernet_container_name = self._get_containernet_container_name(experiment_id)
        try:
            # check that this experiments is not running yet
            if containernet_container_name in self.client.containers.list():
                raise Exception(f"Experiment {experiment_id} is already running")

            containernet_container = self.client.containers.run(
                image="netunicorn/containernet",
                name=containernet_container_name,
                privileged=True,
                pid_mode="host",
                volumes={
                    "/var/run/docker.sock": {
                        "bind": "/var/run/docker.sock",
                        "mode": "rw",
                    },
                    self._get_topology_filename(experiment_id): {
                        "bind": "/custom_topology.py",
                        "mode": "ro",
                    },
                },
                detach=True,
                command=f"python3 /custom_topology.py",
            )

            await asyncio.sleep(2)
            if containernet_container_name not in {x.name for x in self.client.containers.list()}:
                raise Exception(f"Experiment {experiment_id} is not running. Logs: {containernet_container.logs()}")

        except Exception as e:
            self.logger.exception(e)
            return {
                deployment.executor_id: Failure(f"ContainernetConnector exception: {e}")
                for deployment in deployments
            }

        result = {
            deployment.executor_id: Success("Executor probably started - cannot verify as Containernet controls the execution.")
            for deployment in deployments
        }

        return result

    async def stop_executors(
            self,
            username: str,
            requests_list: list[StopExecutorRequest],
            cancellation_context: Optional[dict[str, str]],
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> dict[str, Result[Optional[str], str]]:
        if "experiment_id" not in cancellation_context:
            return {
                request["executor_id"]: Failure(
                    "Containernet connector can stop only the whole experiment, not a single executor. "
                    "Please provide experiment_id in cancellation_context: {'experiment_id': '<experiment_id>'}"
                )
                for request in requests_list
            }
        experiment_id = cancellation_context["experiment_id"]

        try:
            # stop container
            containernet_container_name = self._get_containernet_container_name(experiment_id)
            containernet_container = self.client.containers.get(containernet_container_name)
            containernet_container.stop()
            containernet_container.remove()
        except Exception as e:
            self.logger.exception(e)
            return {
                request["executor_id"]: Failure(f"ContainernetConnector exception: {e}")
                for request in requests_list
            }

        if experiment_id in self.experiment_containers:
            try:
                for container_name in self.experiment_containers[experiment_id]:
                    container = self.client.containers.get(container_name)
                    container.stop()
                    container.remove()
                del self.experiment_containers[experiment_id]
            except Exception:
                pass

        return {
            request["executor_id"]: Success(None)
            for request in requests_list
        }

    async def cleanup(
            self,
            experiment_id: str,
            deployments: list[Deployment],
            *args: Any,
            **kwargs: Any,
    ) -> None:
        # delete containernet container for this experiment_id and all subsequent containers
        try:
            containers = self.client.containers.list()
            for container in containers:
                if (
                        container.name.startswith(self._get_containernet_container_name(experiment_id))
                ):
                    container.stop()
                    container.remove()

            if experiment_id in self.experiment_containers:
                for container_name in self.experiment_containers[experiment_id]:
                    container = self.client.containers.get(container_name)
                    container.stop()
                    container.remove()
                del self.experiment_containers[experiment_id]

        except Exception as e:
            self.logger.exception(e)


async def test_main():
    from netunicorn.base.pipeline import Pipeline
    import uuid

    logger = logging.getLogger('test-logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    connector = ContainernetConnector(
        connector_name='test',
        configuration=None,
        netunicorn_gateway='https://pinot.cs.ucsb.edu/netunicorn',
        logger=logger
    )
    await connector.initialize()
    print(await connector.health())
    nodes = await connector.get_nodes('test')
    for node in nodes:
        print(node.name, node.architecture, node.properties)

    working_node = nodes.take(1)[0]
    working_node.name = "testnodename"

    deployment = Deployment(
        node=working_node,
        pipeline=Pipeline()
    )
    deployment.executor_id = uuid.uuid4().hex
    deployment.prepared = True
    deployment.environment_definition = DockerImage()
    deployment.environment_definition.image = 'netunicorn/executor-template'
    deployment.environment_definition.runtime_context.ports_mapping = {8000: 8000}
    deployment.environment_definition.runtime_context.environment_variables = {'TEST': 'test'}
    deployment_context = {
        'network-definition': json.dumps([
            "s1 = net.addSwitch('s1')",
            "net.addLink(testnodename, s1, cls=TCLink, delay='100ms', bw=1)"
        ])
    }

    print(await connector.deploy('test', 'test', [deployment], deployment_context))
    print(await connector.execute('test', 'test', [deployment], None))
    print(await connector.stop_executors('test', [], {'experiment_id': 'test'}))
    print(await connector.cleanup('test', [deployment]))


if __name__ == '__main__':
    import asyncio

    asyncio.run(test_main())
