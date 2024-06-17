import json
from flask              import Response, Blueprint, jsonify, request
from modules.process    import ProcessesCollector
from dataclasses        import asdict
from ._errors           import *
from server._api_urls   import API_PROCESS, API_PROCESS_CONCRETE



blueprint_process = Blueprint('process', __name__)






@blueprint_process.route(API_PROCESS, methods=['GET'])
def all_processes():
    interval        = request.args.get('path', default=None, type=float)
    processes       = ProcessesCollector(interval).collect()
    return Response(response        = json.dumps([asdict(process) for process in processes], indent=4), 
                    content_type    = "application/json",
                    status          = 200)



@blueprint_process.route(API_PROCESS_CONCRETE, methods=['GET'])
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
