import os

from flask import Flask  # new
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()


# new
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.banking import banking_blueprint
    app.register_blueprint(banking_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
