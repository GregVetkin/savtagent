import json
from flask              import Response, Blueprint, jsonify
from modules.network    import NetConnectionsCollector, NetInterfacesesIOCollector
from dataclasses        import asdict


blueprint_network = Blueprint('network', __name__)



@blueprint_network.route('/network/connections', methods=['GET'])
def all_connections():
    connections         = NetConnectionsCollector().collect()
    connections_json    = json.dumps([asdict(conn) for conn in connections], indent=4)
    return Response(connections_json, content_type="application/json")


@blueprint_network.route('/network/interfaces', methods=['GET'])
def all_interfaces():
    interfaces           = NetInterfacesesIOCollector().collect()
    interfaces_json      = json.dumps([asdict(interface) for interface in interfaces], indent=4)
    return Response(interfaces_json, content_type="application/json")


@blueprint_network.route('/network/interfaces/<string:interface_name>', methods=['GET'])
def one_interface(interface_name):
    interfaces           = NetInterfacesesIOCollector().collect()

    for interface in interfaces:
        if interface.interface == interface_name:
            return jsonify(interface)

    NO_SUCH_INTERFACE = {"error": f"No such interface with name {interface_name}"}
    return jsonify(NO_SUCH_INTERFACE), 404
