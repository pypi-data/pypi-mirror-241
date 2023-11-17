# netunicorn-connector-containernet
This is a netunicorn connector to a Containernet virtual infrastructure.

## User Guide
If your netunicorn installation has enabled Containernet connector, you can use it to create virtual infrastructure
with Containernet. 

You would have an UncountableNodePool object, which (with `__next__` or `take` methods) generates virtual nodes.
You can assign your containers to these virtual nodes and netunicorn will create them in Containernet. You can safely
rename the nodes if needed, the provided name would be used by Containernet.

`WARNING`: the node name should be a valid Python identifier, as you can use it later in your network code to refer to the node.
If the node is not a valid Python identifier, the deployment would fail.

### Network configuration
During deployment, user can provide an arbitrary network configuration using the Containernet syntax:
1. The network configuration string should be provided in the 'network_definition' field of the deployment_context argument of `deploy` method.
2. The network configuration string should represent a JSON-serialized list of strings, where each string is a valid Python line of code for Containernet network configuration.
3. You can refer to your node names in network configuration.
4. You can safely assume, that in the local context of this Python code there exist a Containernet instance with a single controller called `net`.
5. You do not need to start the net execution
6. You do need to create corresponding switches and links for all nodes that should be connected. 
7. If no network configuration is provided, the default network configuration is used. It creates a single switch and connects all nodes to it.

### Usage example
```python
# assuming you already created nodes with names "node1" and "node2"
import json
context = {
  "network_definition": json.dumps([
    "s1 = net.addSwitch('s1')",
    "s2 = net.addSwitch('s2')",
    "net.addLink(node1, s1)",
    "net.addLink(node2, s2)",
    "from mininet.link import TCLink",
    "net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)",
  ])
}

# netunicorn RemoteClient
client.deploy(experiment, 'experiment_name', deployment_context=context)
```

## Administrator guide
Containernet is a network emulator that uses Docker containers to emulate hosts and switches. It allows to create an arbitrary
network topology and set the network parameters for each link.

This package provides a netunicorn connector to Containernet.

### VM-based Installation

**WARNING:** Due to Containernet implementation, it requires to start Containernet Docker container in privileged mode, and 
allows users to run arbitrary Python code inside this container. We **STRICTLY** recommend to run Containernet connector instance 
inside an isolated virtual machine. In this scenario, the Containernet and corresponding connector are running on a virtual 
machine and connector exposes a REST API to netunicorn. The Containernet connector should be started with a API KEY that should be
known to netunicorn instance administrators and specified in connector initialization parameters.

For all instructions below, we assume that you're using a Debian-like virtual machine with port
exposed to netunicorn server.

Inside the virtual machine:
1. Install python3-pip package: `apt install python3-pip`
2. Install openvswitch-switch package: `apt install openvswitch-switch`
3. Install Docker
4. Install connector with rest: `pip3 install netunicorn-connector-containernet[rest]`
5. Start the connector:
    ```bash
    UVICORN_HOST=0.0.0.0 UVICORN_PORT=80 NETUNICORN_API_KEY=h34uyklfba uvicorn netunicorn.director.infrastructure.connectors.containernet.rest:app
    ```
    - `UVICORN_HOST` - IP to bind to
    - `UVICORN_PORT` - port to bind to
    - `NETUNICORN_API_KEY` - API key used for authentication between netunicorn and the connector. Arbitrary string of symbols that should be shared.

On the netunicorn server:
1. Verify that `netunicorn-infrastructure` package is at least of version 0.3.1 (for REST communication)
2. Generate a configuration string for SimpleRESTConnector. This should be a string containing a JSON-serialized dictionary with the following fields:
    - `url`: URL to the connector instance (in this example, exposed port on a virtual machine with Containernet connector instance)
    - `api_key`: API key used for authentication between netunicorn and the connector (in this example, `h34uyklfba`)
    - `init_params`: JSON object with parameters to be passed to the Containernet connector for initialization. Could be omitted.
      - For Containernet, the next parameters are optional:
        - `netunicorn_gateway`: netunicorn gateway endpoint
      - Next parameters are optional:
        - `docker_endpoint`: Docker socket. Default: `unix://var/run/docker.sock`
        - `working_folder`: Folder to store temporary files. Default: `/tmp`  

    The simplest example of the configuration:  
    ```json
    {
      "url": "http://192.168.0.3/",
      "api_key": "h34uyklfba"
    }
    ```

    The example with additional parameters:
    ```json
    {
      "url": "http://192.168.0.3/",
      "api_key": "h34uyklfba",
      "init_params": {
        "netunicorn_gateway": "http://192.168.0.2/netunicorn",
        "docker_endpoint": "unix://var/run/docker.sock",
        "working_folder": "/somefolder"
      }
    }
    ```

3. Correctly initialize a SimpleRESTConnector connector:
    ```yaml
    netunicorn.infrastructure.connectors:
      containernet:
        enabled: true
        module: "netunicorn.director.infrastructure.connectors.rest"  # where to import from
        class: "SimpleRESTConnector"  # class name
        config: '{"url": "http://192.168.0.3/", "api_key": "h34uyklfba"}'  # configuration string from the previous step
    ```
