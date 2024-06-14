import os
import json
from dataclasses        import asdict
from flask              import Blueprint, Response, request
from modules.file       import FileInfoCollector
from ._errors           import *


blueprint_file = Blueprint('file', __name__)





@blueprint_file.route('/system/fileinfo', methods=['GET'])
def cpu_usage():
    file_path   = request.args.get('path', default=None, type=str)
    hashalg     = request.args.get('hashalg', default=None, type=str)
    
    if not file_path and os.path.isfile(file_path):
        return Response(response        = json.dumps(BAD_FILE_PATH, indent=4), 
                        content_type    = "application/json",
                        status          = 404)
    
    if not os.path.exists(file_path):
        return Response(response        = json.dumps(FILE_NOT_FOUND, indent=4), 
                        content_type    = "application/json",
                        status          = 404)
    
    if hashalg not in [None, "md5", "sha256"]:
        return Response(response        = json.dumps(NO_SUCH_ALGORITHM, indent=4), 
                        content_type    = "application/json",
                        status          = 404)
    
    file_data       = FileInfoCollector(file_path, hashalg).collect()
    return Response(response        = json.dumps(asdict(file_data), indent=4), 
                    content_type    = "application/json",
                    status          = 200)
