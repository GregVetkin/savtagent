import json
from dataclasses        import asdict
from flask              import Blueprint, request, Response
from modules.cpu        import CpuUsageCollector


blueprint_cpu = Blueprint('cpu', __name__)




@blueprint_cpu.route('/cpu/usage', methods=['GET'])
def cpu_usage():
    interval    = request.args.get('interval', default=None, type=float)
    usage       = CpuUsageCollector(interval).collect()
    return Response(response        = json.dumps(asdict(usage), indent=4), 
                    content_type    = "application/json",
                    status          = 200)

