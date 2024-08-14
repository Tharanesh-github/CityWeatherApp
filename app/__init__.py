# app/__init__.py

from flask import Flask
from app.config import Config
from app.controllers.weather_controller import weather_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registering blueprints
    app.register_blueprint(weather_bp, url_prefix='/api')

    return app
