from flaskapi.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_class=Config):
    """
    Initiate application and register the routes and handlers to blueprint
    :param config_class: settings for SQL
    :return: application initiate and blueprint mapping
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from flaskapi.api.routes import api
    from flaskapi.errors.handlers import errors

    app.register_blueprint(api)
    app.register_blueprint(errors)

    return app
