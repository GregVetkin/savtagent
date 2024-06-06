from flask              import Blueprint, jsonify, request
from modules.file       import FileInfoCollector
import os


blueprint_file = Blueprint('file', __name__)




@blueprint_file.route('/file/info', methods=['GET'])
def cpu_usage():
    file_path   = request.args.get('path', default=None, type=str)
    hashalg     = request.args.get('hashalg', default=None, type=str)
    
    if not file_path and os.path.isfile(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    if hashalg not in [None, "md5", "sha256"]:
        return jsonify({'error': 'No such hash algorithm. Available: md5, sha256'}), 404
    
    file_data       = FileInfoCollector(file_path, hashalg).collect()
    return jsonify(file_data)
