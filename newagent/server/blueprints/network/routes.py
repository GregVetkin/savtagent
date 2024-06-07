import json
from dataclasses        import asdict
from flask              import Response, Blueprint
from modules.network    import NetConnectionsCollector, NetInterfacesesIOCollector



blueprint_network = Blueprint('network', __name__)


NO_SUCH_INTERFACE = {"error": "No such interface"}


@blueprint_network.route('/network/connections', methods=['GET'])
def all_connections():
    connections = NetConnectionsCollector().collect()
    return Response(response        = json.dumps([asdict(conn) for conn in connections], indent=4), 
                    content_type    = "application/json",
                    status          = 200)


@blueprint_network.route('/network/interface', methods=['GET'])
def all_interfaces():
    interfaces = NetInterfacesesIOCollector().collect()
    return Response(response        = json.dumps([asdict(interface) for interface in interfaces], indent=4), 
                    content_type    = "application/json",
                    status          = 200)



@blueprint_network.route('/network/interface/<string:interface_name>', methods=['GET'])
def one_interface(interface_name):
    interfaces = NetInterfacesesIOCollector().collect()
    for interface in interfaces:
        if interface.interface == interface_name:
            return Response(response        = json.dumps(asdict(interface), indent=4), 
                            content_type    = "application/json",
                            status          = 200)

    return Response(response        = json.dumps(NO_SUCH_INTERFACE, indent=4), 
                    content_type    = "application/json",
                    status          = 404)

