
from flask import Flask
from ndf.blueprint.joke import joke

def create_app():
    """creates an instance of the app.

    returns app instance"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.prod_settings")
    app.register_blueprint(joke)
    return app
