# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flaskpoc'

    # Register blueprints
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
