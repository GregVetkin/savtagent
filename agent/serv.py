from flask import Flask, jsonify, Response, request
import os
import json
from src.collectors import ProcessesCollector, CpuUsageCollector, MemoryCollector, NetInterfacesesIOCollector, DisksCollector, DataCollector, NetConnectionsCollector, FileInfoCollector




app = Flask(__name__)



@app.route('/memory', methods=['GET'])
def memory():
    mem = MemoryCollector.collect()
    json_string = json.dumps(mem.__dict__, default=lambda x: x.__dict__)
    return Response(json_string, content_type="application/json")


@app.route('/processes', methods=['GET'])
def processes():
    procs = ProcessesCollector.collect()
    return jsonify(procs)


@app.route('/fileinfo', methods=['GET'])
def file_info():
    file_path   = request.args.get('path')
    hashalg     = request.args.get('hashalg')
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    
    fileinfo = FileInfoCollector(file_path, hashalg).collect()

    return jsonify(fileinfo)




if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8081
    app.run(host=HOST, port=PORT, debug=True)