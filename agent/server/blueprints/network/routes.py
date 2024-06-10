import json
from dataclasses        import asdict
from flask              import Response, Blueprint
from modules.network    import NetConnectionsCollector, NetInterfacesesIOCollector
from modules.tools      import check_ip_collisions_threads, threading_ip_duplication


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



@blueprint_network.route('/network/collisions', methods=['GET'])
def ip_collisions():
    try:
        collisions = threading_ip_duplication()
    except Exception as e:
        return Response(response        = json.dumps({"error": str(e)}, indent=4), 
                        content_type    = "application/json",
                        status          = 500)
    else:
        return Response(response        = json.dumps(collisions, indent=4), 
                        content_type    = "application/json",
                        status          = 200)