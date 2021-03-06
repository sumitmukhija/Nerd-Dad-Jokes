
from flask import Flask
from ndf.blueprint.joke import joke

def create_app():
    """creates an instance of the app.

    returns app instance"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.settings")
    app.register_blueprint(joke)
    return app

if __name__ == "__main__":
    application = create_app()
    application.run(host='0.0.0.0', port=80)
    