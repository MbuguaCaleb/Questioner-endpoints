import os
from flask import Flask, jsonify
from instance.config import app_config
from app.api.v1.views.meetup_view import v1 as meetups_blueprint_v1
from app.api.v1.views.questions_views import v1 as questions_blueprint_v1
from app.api.v1.views.user_views import v1 as users_blueprint_v1

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
    app.register_blueprint(users_blueprint_v1)

    @app.errorhandler(404)
    def page_not_found(error):
        """ Handler for error 404 """

        return jsonify({'status': 404, 'message': 'The requested page was not found'}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        """ Handler for error 405 """

        return jsonify({'status': 405, 'message': 'Method not allowed'}), 405

    
    @app.errorhandler(400)
    def method_not_allowed(error):
        """ Handler for error 405 """

        return jsonify({'status': 400, 'message': 'Method not allowed'}), 405
    
    
    @app.errorhandler(401)
    def method_not_allowed(error):
        """ Handler for error 405 """

        return jsonify({'status': 401, 'message': 'Unauthorised success'}), 401
    
    
    @app.errorhandler(403)
    def method_not_allowed(error):
        """ Handler for error 405 """

        return jsonify({'status': 403, 'Forbidden': 'oops!Forbidden'}), 403


    return app

