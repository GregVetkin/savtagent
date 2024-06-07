from flask                          import Flask, Blueprint
from flask_cors                     import CORS
from typing                         import List


from .blueprints.memory.routes      import blueprint_memory
from .blueprints.cpu.routes         import blueprint_cpu
from .blueprints.file.routes        import blueprint_file
from .blueprints.storage.routes     import blueprint_storage
from .blueprints.process.routes     import blueprint_process
from .blueprints.network.routes     import blueprint_network

APP         = Flask(__name__)
HOST        = '0.0.0.0'
PORT        = 8081
DEBUG       = True
BLUEPRINTS  = [
    blueprint_memory,
    blueprint_cpu,
    blueprint_file,
    blueprint_storage,
    blueprint_process,
    blueprint_network,
]
CORS(APP)


def register_blueprints(app: Flask, blueprints: List[Blueprint]):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def run_server(app: Flask):
    app.run(host=HOST, port=PORT, debug=DEBUG)


def run():
    register_blueprints(APP, BLUEPRINTS)
    run_server(APP)



if __name__ == '__main__':
    run()
