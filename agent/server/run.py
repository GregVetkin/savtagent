from flask              import Flask
from flask_cors         import CORS
from .blueprint         import init_routes
from .routes            import BLUEPRINT


APP     = Flask(__name__)
CORS(APP)

HOST    = '0.0.0.0'
PORT    = 8081
DEBUG   = True

    
# Инициализация маршрутов
init_routes(APP, BLUEPRINT)


def run_server():
    APP.run(host=HOST, port=PORT, debug=DEBUG)


if __name__ == '__main__':
    run_server()
