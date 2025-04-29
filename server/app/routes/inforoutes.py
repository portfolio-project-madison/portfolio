from flask import Blueprint, request, jsonify 
from flask_cors import cross_origin

info_bp = Blueprint('info', __name__)

@info_bp.route('/social', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_socials():

  return jsonify([
        {"title": "LinkedIn", "link": "https://www.linkedin.com/in/madison-tolentino-293139257/"},
        {"title": "Github", "link": "https://github.com/madisonnnn"}
    ])

@info_bp.route('/software-projects', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_projects():

  return jsonify([
        {"title": "Project One", "description": "Description of project one."},
        {"title": "Project Two", "description": "Description of project two."}
    ])

@info_bp.route('/additional-projects', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_additional():

  return jsonify([
        {"title": "Project One", "description": "Description of project one."},
        {"title": "Project Two", "description": "Description of project two."}
    ])

@info_bp.route('/tech-competencies', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_competencies():

  return jsonify([
        {"title": "Project One", "description": "Description of project one."},
        {"title": "Project Two", "description": "Description of project two."}
    ])

@info_bp.route('/bio', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_bio():

  return jsonify([
        {"title": "Project One", "description": "Description of project one."},
        {"title": "Project Two", "description": "Description of project two."}
    ])
