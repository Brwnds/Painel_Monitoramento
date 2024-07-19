from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

    return app

from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Permite solicitações do frontend
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

    return app


