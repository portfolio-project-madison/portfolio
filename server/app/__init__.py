import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
from server.app.routes.inforoutes import info_bp

def create_app():
    app = Flask(__name__,  static_folder='server/app/static/dist', static_url_path='')
    CORS(app)
  
    # Initialize extensions with the app

    # Import models after db initialization
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_frontend(path):
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')
    # Register Blueprints

    app.register_blueprint(info_bp, url_prefix='/info')
    return app