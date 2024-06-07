import json
from dataclasses        import asdict
from flask              import Response, Blueprint, jsonify
from modules.storage    import DisksInfoCollector



blueprint_storage = Blueprint('storage', __name__)



@blueprint_storage.route('/storage', methods=['GET'])
def all_disks_data():
    disks = DisksInfoCollector().collect()
    return Response(response        = json.dumps([asdict(disk) for disk in disks], indent=4), 
                    content_type    = "application/json",
                    status          = 200)




