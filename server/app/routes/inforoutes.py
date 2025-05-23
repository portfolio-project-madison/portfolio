from flask import Blueprint, request, jsonify, url_for
from flask_cors import cross_origin

info_bp = Blueprint('info', __name__)

@info_bp.route('/social', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_socials():

  return jsonify([
        {"title": "LinkedIn", "link": "https://www.linkedin.com/in/madison-tolentino-293139257/"},
        {"title": "Github", "link": "https://github.com/madisonnnn"},
        {"title": "Dev.To", "link": "https://dev.to/madison_tolentino_d23fca7"},
        {"title": "Email", "link": "madisontolentino@gmail.com"}
    ])

@info_bp.route('/software-projects', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_projects():

  return jsonify([
        {"title": "Burgle", "link": "https://github.com/BurgleProject/Project"},
        {"title": "Pacemates", "link": "https://github.com/CivicTechMM/PaceMates"},
        {"title": "Burgl!:Remastered!", "link": "https://github.com/burgle-remastered/burgle-remastered-project"}
    ])

@info_bp.route('/additional-projects', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_additional():

  return jsonify([
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Lucy", "link": url_for('static', filename='images/lucy.png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Chainsawman", "link": url_for('static', filename='images/Chainsawman.png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Inosuke", "link": url_for('static', filename='images/Inosuke-1.png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Gojo", "link": url_for('static', filename='images/Gojo_(2)-1[1].png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Soul Eater", "link": url_for('static', filename='images/soul eater [Recovered]-1.png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Ouran High School Host Club", "link": url_for('static', filename='images/ohshc_[Recovered]-1[1].png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Little Witch Academia", "link": url_for('static', filename='images/LWA [Recovered].png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Mystic Messenger", "link": url_for('static', filename='images/707.png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "High Rise Invasion", "link": url_for('static', filename='images/mayu.png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"ai","title": "Midari", "link": url_for('static', filename='images/Midari.png', _external=True)},
        {"bio":"This is a sample sentence intended to serve as default text in a design or layout, providing a visual sense of how content might appear in a finished project. It continues with a second sentence that adds more length and structure, helping to demonstrate how multiple lines of text will look within the overall composition.","type":"yt","title": "Youtube", "link": "https://www.youtube.com/@silvxx-1247"},
    ])

@info_bp.route('/tech-competencies', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_competencies():

  return jsonify([
        {"title": "Javascript", "type": "Languages and Databases"},
        {"title": "Python", "type": "Languages and Databases"},
        {"title": "HTML", "type": "Languages and Databases"},
        {"title": "CSS", "type": "Languages and Databases"},
        {"title": "SQL", "type": "Languages and Databases"},
        {"title": "Unity", "type": "Languages and Databases"},
        {"title": "Git", "type": "Tools and Testing"},
        {"title": "OOP", "type": "Tools and Testing"},
        {"title": "React.js", "type": "Frameworks and Libraries"},
        {"title": "Node.js", "type": "Frameworks and Libraries"},
        {"title": "Express.js", "type": "Frameworks and Libraries"},
        {"title": "Knex.js", "type": "Frameworks and Libraries"},
        {"title": "Bcrypt", "type": "Frameworks and Libraries"},
        {"title": "Flask", "type": "Frameworks and Libraries"},
        {"title": "Adobe Illustrator", "type": "Additional"},
        {"title": "Figma", "type": "Additional"},
        {"title": "Audacity", "type": "Additional"},
        {"title": "Videopad", "type": "Additional"},
        {"title": "Klaviyo", "type": "Additional"},
    ])

@info_bp.route('/bio', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_bio():

  return jsonify([
        {"bio": "im madison!!!!"}
    ])
