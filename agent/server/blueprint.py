from flask import Blueprint


def get_blueprint():
    return Blueprint('main', __name__)


def init_routes(app, blueprint):
    app.register_blueprint(blueprint)
