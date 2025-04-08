from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(__name__)
    CORS(app)
  
    # Initialize extensions with the app

    # Import models after db initialization


# Register Blueprints
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    # app.register_blueprint(burger_bp, url_prefix='/burger')
    
    return app