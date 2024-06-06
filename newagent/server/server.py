from flask                          import Flask, Blueprint
from flask_cors                     import CORS
from typing                         import List


from .blueprints.memory.routes      import memory_blueprint
from .blueprints.cpu.routes         import cpu_blueprint
from .blueprints.file.routes        import file_blueprint



APP     = Flask(__name__)
CORS(APP)

HOST    = '0.0.0.0'
PORT    = 8081
DEBUG   = True

BLUEPRINTS = [
    memory_blueprint,
    cpu_blueprint,
    file_blueprint,
]


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
