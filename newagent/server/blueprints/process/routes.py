import json
from flask              import Response, Blueprint, jsonify, request
from modules.process    import ProcessesCollector
from dataclasses        import asdict



blueprint_process = Blueprint('process', __name__)



@blueprint_process.route('/process', methods=['GET'])
def all_processes():
    interval        = request.args.get('path', default=None, type=float)
    processes       = ProcessesCollector(interval).collect()
    json_string     = json.dumps([asdict(process) for process in processes], indent=4)
    return Response(json_string, content_type="application/json")


@blueprint_process.route('/process/<int:pid>', methods=['GET'])
def pid_process(pid):
    interval  = request.args.get('path', default=None, type=float)
    processes = ProcessesCollector(interval).collect()

    for process in processes:
        if process.pid == pid:
            return jsonify(process)

    NO_SUCH_PROCESS = {"error": f"No such process with pid {pid}"}
    return jsonify(NO_SUCH_PROCESS), 404