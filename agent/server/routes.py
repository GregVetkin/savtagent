import json
import os
from dataclasses      import asdict
from flask            import Response, jsonify, request
from .blueprint       import get_blueprint
from src.tools        import shutdown, reboot, notification, journalctl_logs
from src.collectors   import (MemoryCollector, 
                              CpuUsageCollector, 
                              DisksCollector, 
                              NetConnectionsCollector, 
                              NetInterfacesesIOCollector, 
                              ProcessesCollector, 
                              FileInfoCollector)



# Создаем экземпляр Blueprint
BLUEPRINT = get_blueprint()


@BLUEPRINT.route('/health', methods=['GET'])
def server_health():
    return "OK"


@BLUEPRINT.route('/memory', methods=['GET'])
def get_memory():
    memory      = MemoryCollector.collect()
    json_string = json.dumps(asdict(memory), indent=4)
    return Response(json_string, content_type="application/json")


@BLUEPRINT.route('/processes', methods=['GET'])
def get_processes():
    procs = ProcessesCollector.collect()
    return jsonify(procs)


@BLUEPRINT.route('/fileinfo', methods=['GET'])
def get_fileinfo():
    file_path   = request.args.get('path')
    hashalg     = request.args.get('hashalg')
    
    if not file_path and os.path.isfile(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    if hashalg not in [None, "md5", "sha256"]:
        return jsonify({'error': 'No such hash algorithm. Available: md5, sha256'}), 404
    
    fileinfo = FileInfoCollector(file_path, hashalg).collect()

    return jsonify(fileinfo)


@BLUEPRINT.route('/cpuusage', methods=['GET'])
def get_cpuusage():
    cpu_usage = CpuUsageCollector.collect()
    return jsonify(cpu_usage)


@BLUEPRINT.route('/disks', methods=['GET'])
def get_disksinfo():
    disks           = DisksCollector.collect()
    disks_dict_list = [asdict(disk) for disk in disks]
    disks_json      = json.dumps(disks_dict_list, indent=4)
    return Response(disks_json, content_type="application/json")


@BLUEPRINT.route('/connections', methods=['GET'])
def get_connections():
    connections         = NetConnectionsCollector.collect()
    conn_dict_list      = [asdict(conn) for conn in connections]
    connections_json    = json.dumps(conn_dict_list, indent=4)
    return Response(connections_json, content_type="application/json")


@BLUEPRINT.route('/network', methods=['GET'])
def get_network():
    interfaces           = NetInterfacesesIOCollector.collect()
    interfaces_dict_list = [asdict(interface) for interface in interfaces]
    interfaces_json      = json.dumps(interfaces_dict_list, indent=4)
    return Response(interfaces_json, content_type="application/json")



@BLUEPRINT.route('/message', methods=['GET'])
def send_notification():
    title   = request.args.get('title')
    text    = request.args.get('text')

    if title is None:
        return jsonify({'error': 'No title'}), 404
    if text is None:
        return jsonify({'error': 'No text message'}), 404

    notification(title, text)

    return "OK"


@BLUEPRINT.route('/shutdown', methods=['GET'])
def shutdown_pc():
    shutdown()
    return "OK"


@BLUEPRINT.route('/reboot', methods=['GET'])
def reboot_pc():
    reboot()
    return "OK"



@BLUEPRINT.route('/logs', methods=['GET'])
def get_journalctl_logs():
    since       = request.args.get('since')
    until       = request.args.get('until')
    priority    = request.args.get('priority')
    lines       = request.args.get('lines')
    unit        = request.args.get('unit')

    if priority not in ["0", "1", "2", "3", "4", "5", "6", "7", 
                        "debug", "info", "notice", "warning", "err", "crit", "alert", "emerg"]:
        return jsonify({'error': 'Bad priority. Accepted: 0, 1, 2, 3, 4, 5, 6, 7, debug, info, notice, warning, err, crit, alert, emerg'})


    logs        = journalctl_logs(since, until, priority, lines, unit)
    return jsonify(logs)

