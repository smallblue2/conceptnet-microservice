from flask import Flask
from .services.query import query_blueprint
import os

# Factory function for our app
def create_app():
    # Create our WSGI object
    app = Flask(__name__)

    # Configurations for the microservice
    app.config['CONCEPTNET_API_URL'] = os.getenv('CONCEPTNET_API_URL')
    app.config['CONCEPTNET_LANG_FILTER'] = os.getenv('CONCEPTNET_LANG_FILTER')

    # Register different blueprints (functionalities) of our service
    app.register_blueprint(query_blueprint)

    return app
