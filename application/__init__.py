from flask import Flask
from .config import config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    from .views import api

    app.register_blueprint(api.api_blueprint)

    return app
