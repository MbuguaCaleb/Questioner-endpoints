import os
from flask import Flask, jsonify
from instance.config import app_config
from flask_jwt_extended import (JWTManager)
from app.api.v1.views.meetup_view import v1 as meetups_blueprint_v1
from app.api.v1.views.questions_views import v1 as questions_blueprint_v1

def create_app(config_name):
    """ Function to initialize Flask app """

    config_name = os.environ.get('FLASK_CONFIG', 'development')

    # Initialize app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

 
    # Register V1 Blueprints
    app.register_blueprint(meetups_blueprint_v1)
    app.register_blueprint(questions_blueprint_v1)
    

    return app



    