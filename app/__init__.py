import os

from flask import Flask

from instance.config import app_config

def create_app(config):
    '''function creating the flask app'''
    
    config_name = os.environ.get('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    
    app.config.from_object(app_config[config_name])
    
    return app

