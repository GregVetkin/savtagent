from flask              import Blueprint, jsonify, request
from modules.cpu        import CpuUsageCollector


blueprint_cpu = Blueprint('cpu', __name__)




@blueprint_cpu.route('/cpu/usage', methods=['GET'])
def cpu_usage():
    interval    = request.args.get('interval', default=None, type=float)
    usage       = CpuUsageCollector(interval).collect()
    return jsonify(usage)

