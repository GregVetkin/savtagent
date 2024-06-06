import json

from dataclasses        import asdict
from flask              import Response, jsonify, request
from ..blueprint        import get_blueprint
from modules.memory     import MemoryCollector



# Создаем экземпляр Blueprint
BLUEPRINT = get_blueprint()


@BLUEPRINT.route('/memory', methods=['GET'])
def get_memory():
    memory      = MemoryCollector().collect()
    json_string = json.dumps(asdict(memory), indent=4)
    return Response(json_string, content_type="application/json")