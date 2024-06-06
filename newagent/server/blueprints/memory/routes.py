import json
from dataclasses        import asdict
from flask              import Response, Blueprint, jsonify
from modules.memory     import MemoryCollector, RamMemoryCollector, SwapMemoryCollector



blueprint_memory = Blueprint('memory', __name__)




@blueprint_memory.route('/memory', methods=['GET'])
def all_memory():
    memory      = MemoryCollector().collect()
    json_string = json.dumps(asdict(memory), indent=4)
    return Response(json_string, content_type="application/json")


@blueprint_memory.route('/memory/ram', methods=['GET'])
def ram_memory():
    ram      = RamMemoryCollector().collect()
    return jsonify(ram)


@blueprint_memory.route('/memory/swap', methods=['GET'])
def swap_memory():
    swap      = SwapMemoryCollector().collect()
    return jsonify(swap)
