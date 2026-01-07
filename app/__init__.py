# app/__init__.py
import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # Register blueprints
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
