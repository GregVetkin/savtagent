import os
import json
import re
from dataclasses        import asdict
from flask              import Blueprint, Response, request
from modules.file       import FileInfoCollector, FileRegexCollector
from ._errors           import *
from server._api_urls   import API_FILE_INFO, API_FILE_REGEX

blueprint_file = Blueprint('file', __name__)





@blueprint_file.route(API_FILE_INFO, methods=['GET'])
def file_info():
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



@blueprint_file.route(API_FILE_REGEX, methods=['GET'])
def file_regx():
    file_path   = request.args.get('path', default=None, type=str)
    pattern     = request.args.get('pattern', default=None, type=str)

    if not file_path and os.path.isfile(file_path):
        return Response(response        = json.dumps(BAD_FILE_PATH, indent=4), 
                        content_type    = "application/json",
                        status          = 404)
    
    if not os.path.exists(file_path):
        return Response(response        = json.dumps(FILE_NOT_FOUND, indent=4), 
                        content_type    = "application/json",
                        status          = 404)
    
    try:
        re.compile(pattern)
    except re.error as e:
        return Response(response        = json.dumps(BAD_PATTERN, indent=4), 
                        content_type    = "application/json",
                        status          = 404)
    try:
        coincidences = FileRegexCollector(file_path, pattern).collect()
    except Exception as e:
        return Response(response        = json.dumps(str(e), indent=4), 
                        content_type    = "application/json",
                        status          = 500)
    else:
        return Response(response        = json.dumps(coincidences, indent=4), 
                        content_type    = "application/json",
                        status          = 200)