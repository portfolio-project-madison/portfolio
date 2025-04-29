from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from app.routes.inforoutes import info_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
  
    # Initialize extensions with the app

    # Import models after db initialization


# Register Blueprints
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(info_bp, url_prefix='/info')
    
    return app