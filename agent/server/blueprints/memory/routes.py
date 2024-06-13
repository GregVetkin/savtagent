import json
from dataclasses        import asdict
from flask              import Response, Blueprint
from modules.memory     import MemoryCollector, RamMemoryCollector, SwapMemoryCollector



blueprint_memory = Blueprint('memory', __name__)




@blueprint_memory.route('/memory', methods=['GET'])
def all_memory():
    memory = MemoryCollector().collect()
    return Response(response        = json.dumps(asdict(memory), indent=4), 
                    content_type    = "application/json",
                    status          = 200)


@blueprint_memory.route('/memory/ram', methods=['GET'])
def ram_memory():
    ram = RamMemoryCollector().collect()
    return Response(response        = json.dumps(asdict(ram), indent=4), 
                    content_type    = "application/json",
                    status          = 200)


@blueprint_memory.route('/memory/swap', methods=['GET'])
def swap_memory():
    swap = SwapMemoryCollector().collect()
    return Response(response        = json.dumps(asdict(swap), indent=4), 
                    content_type    = "application/json",
                    status          = 200)
