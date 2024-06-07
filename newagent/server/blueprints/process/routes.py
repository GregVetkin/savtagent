import json
from flask              import Response, Blueprint, jsonify, request
from modules.process    import ProcessesCollector
from dataclasses        import asdict



blueprint_process = Blueprint('process', __name__)

NO_SUCH_PROCESS = {"error": "No such process"}




@blueprint_process.route('/process', methods=['GET'])
def all_processes():
    interval        = request.args.get('path', default=None, type=float)
    processes       = ProcessesCollector(interval).collect()
    return Response(response        = json.dumps([asdict(process) for process in processes], indent=4), 
                    content_type    = "application/json",
                    status          = 200)



@blueprint_process.route('/process/<int:pid>', methods=['GET'])
def pid_process(pid):
    interval  = request.args.get('path', default=None, type=float)

    for process in ProcessesCollector(interval).collect():
        if process.pid == pid:
            return Response(response        = json.dumps(asdict(process), indent=4), 
                            content_type    = "application/json",
                            status          = 200)

    
    return Response(response        = json.dumps(asdict(NO_SUCH_PROCESS), indent=4), 
                    content_type    = "application/json",
                    status          = 404)
