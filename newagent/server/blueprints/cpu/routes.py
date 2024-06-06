from flask              import Blueprint, jsonify, request
from modules.cpu        import CpuUsageCollector


cpu_blueprint = Blueprint('cpu', __name__)




@cpu_blueprint.route('/cpu/usage', methods=['GET'])
def cpu_usage():
    interval    = request.args.get('interval', default=None, type=float)
    usage       = CpuUsageCollector(interval).collect()
    return jsonify(usage)

