import json
from flask              import Response, Blueprint, jsonify, request
from modules.process    import ProcessesCollector
from dataclasses        import asdict



blueprint_process = Blueprint('process', __name__)

<<<<<<< HEAD
=======
NO_SUCH_PROCESS = {"error": "No such process"}

>>>>>>> 99d8e1f (Added processes and network)


@blueprint_process.route('/process', methods=['GET'])
def all_processes():
    interval        = request.args.get('path', default=None, type=float)
    processes       = ProcessesCollector(interval).collect()
<<<<<<< HEAD
    json_string     = json.dumps([asdict(process) for process in processes], indent=4)
    return Response(json_string, content_type="application/json")
=======
    return Response(response        = json.dumps([asdict(process) for process in processes], indent=4), 
                    content_type    = "application/json",
                    status          = 200)
>>>>>>> 99d8e1f (Added processes and network)


@blueprint_process.route('/process/<int:pid>', methods=['GET'])
def pid_process(pid):
    interval  = request.args.get('path', default=None, type=float)
    processes = ProcessesCollector(interval).collect()
<<<<<<< HEAD

    for process in processes:
        if process.pid == pid:
            return jsonify(process)

    NO_SUCH_PROCESS = {"error": f"No such process with pid {pid}"}
    return jsonify(NO_SUCH_PROCESS), 404
=======
    for process in processes:
        if process.pid == pid:
            return Response(response        = json.dumps(asdict(process), indent=4), 
                            content_type    = "application/json",
                            status          = 200)

    
    return Response(response        = json.dumps(asdict(NO_SUCH_PROCESS), indent=4), 
                    content_type    = "application/json",
                    status          = 404)
>>>>>>> 99d8e1f (Added processes and network)
