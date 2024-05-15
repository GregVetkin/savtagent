from flask import Flask, jsonify, Response
import json
from src.collectors import ProcessesCollector, CpuUsageCollector, MemoryCollector, NetInterfacesesIOCollector, DisksCollector, DataCollector, NetConnectionsCollector




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


HOST = '0.0.0.0'
PORT = 8080


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)