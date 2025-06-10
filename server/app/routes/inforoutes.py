from flask import Blueprint, request, jsonify, url_for
from flask_cors import cross_origin

info_bp = Blueprint('info', __name__)

@info_bp.route('/social', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_socials():

  return jsonify([
        {"img":url_for('static', filename='images/linkedin.png', _external=True),"title": "LinkedIn", "link": "https://www.linkedin.com/in/madison-tolentino-293139257/"},
        {"img":url_for('static', filename='images/github.png', _external=True),"title": "Github", "link": "https://github.com/madisonnnn"},
        {"img":url_for('static', filename='images/devto.png', _external=True),"title": "Dev.To", "link": "https://dev.to/madison_tolentino_d23fca7"},
        {"img":url_for('static', filename='images/gmail.png', _external=True),"title": "Email", "link": "madisontolentino@gmail.com"}
    ])

@info_bp.route('/software-projects', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_projects():

  return jsonify([
        {"img":url_for('static', filename='images/burgl.jpeg', _external=True),"title": "Burgl!:Remastered!", "link": "https://github.com/burgle-remastered/burgle-remastered-project","bio":"Burgl!:Remastered! is the improved Burgle!; An interactive journaling app aimed to empower neurodivergent individuals. We use the components of a burger to structure your day, as well as a daily spoon count to measure your energy levels. We used 3D props you can spin around to get you addicted to this good habit! \n\nTechnologies Used: html, css, React, Javascript, Figma, Python, Blender, ThreeJs, Flask, React Three Fiber, Postgressql"},
        {"img":url_for('static', filename='images/pacemates.png', _external=True),"title": "Pacemates", "link": "https://github.com/CivicTechMM/PaceMates","bio":"PaceMates is a running app created to support those struggling with mental health. Our website provides a safe space where individuals can join communities and create/participate in events based on common athletic interests. \n\nTechnologies Used: html, css, React, Javascript, Figma, Express, Postgressql, Knex"},
        {"img":url_for('static', filename='images/burgle.jpeg', _external=True),"title": "Burgle!", "link": "https://github.com/BurgleProject/Project","bio":"Burgle! is the original of \"Burgl!:Remastered!\". This project was essentially the prototype, made before we deepened our skills further. This is a less complex version, which also features a daily burger and spoon count for your journaling needs. \n\nTechnologies Used: html, css, React, Javascript, Figma"}    
    ])

@info_bp.route('/additional-projects', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_additional():

  return jsonify([
        {"bio":"This is Lucy! She's a super cool character from Cyberpunk: Edgerunners, an amazing anime based of the Cyberpunk game itself! She's the first Adobe Illustrator project that I created :)","type":"ai","title": "Lucy", "link": url_for('static', filename='images/lucy.png', _external=True)},
        {"bio":"Here is the one and only Chainsawman! An anime I haven't even finished (please don't hate me), but love so much. I love the detail in this one!","type":"ai","title": "Chainsawman", "link": url_for('static', filename='images/Chainsawman.png', _external=True)},
        {"bio":"The best Demon Slayer character in my opinion right here: Inosuke! This project pushed me to have a better understanding of layers and opacity to add more depth to my art :)","type":"ai","title": "Inosuke", "link": url_for('static', filename='images/Inosuke-1.png', _external=True)},
        {"bio":"Gojo!! An absolute top tier character and very silly. Here I learned that creating characters was definitely my favorite part of making these pieces...","type":"ai","title": "Gojo", "link": url_for('static', filename='images/Gojo_(2)-1[1].png', _external=True)},
        {"bio":"And here's my guilty pleasure project! I loved every second of making this and spent most of my days working on it. I spent so much time on it I finished it in a week! Nothing is more rewarding than seeing all of your blobs finally look like a person.","type":"ai","title": "Soul Eater", "link": url_for('static', filename='images/soul eater [Recovered]-1.png', _external=True)},
        {"bio":"This is Ouran High School Host Club, an anime I hold dear to my heart. This is the only project thats a combination of two references!","type":"ai","title": "Ouran High School Host Club", "link": url_for('static', filename='images/ohshc_[Recovered]-1[1].png', _external=True)},
        {"bio":"Here are some of the main characters from Little Witch Academia, a silly anime about a girls' lifelong dream to become a witch! I chose this image so I could improve on my background-making skills, but creating details in a wood floor definitely burnt me out...","type":"ai","title": "Little Witch Academia", "link": url_for('static', filename='images/LWA [Recovered].png', _external=True)},
        {"bio":"So I went back to a guitly pleasure! Here is 707, or Saeyoung Choi, from Mystic Messenger; a mobile,rpg game with a fascinating storyline, the silliest of characters, and a vast amount of choices to make that'll impact how the game goes!","type":"ai","title": "Mystic Messenger", "link": url_for('static', filename='images/707.png', _external=True)},
        {"bio":"This is Mayu from High Rise Invasion, a Netflix Original anime that still doesn't have a season two... But I absolutely love the context of this show and I totally recommend it.","type":"ai","title": "High Rise Invasion", "link": url_for('static', filename='images/mayu.png', _external=True)},
        {"bio":"And last but not least we have Midari from Kakegurui! She's one of the more insane characters, but she has a special place in my heart.","type":"ai","title": "Midari", "link": url_for('static', filename='images/Midari.png', _external=True)},
        {"bio":"This is my YouTube Channel! It's been a while, but I used to make slowed and reverbed versions of songs! I did this for about two years until I could unfortunately no longer afford the programs necessary to create the videos. However, I still love making videos and I would definitely get back into it! Just click the title to find my channel :)","type":"yt","title": "Youtube", "link": "https://www.youtube.com/@silvxx-1247",'img':url_for('static', filename='images/tzuyu.jpg', _external=True)},
    ])

@info_bp.route('/tech-competencies', methods = ['POST','GET'])
@cross_origin(methods=['POST','GET'], supports_credentials=True, origin='http://127.0.0.1:5000')
def get_competencies():

  return jsonify([
        {"title": "Javascript", "type": "Languages and Databases"},
        {"title": "Python", "type": "Languages and Databases"},
        {"title": "Html", "type": "Languages and Databases"},
        {"title": "Css", "type": "Languages and Databases"},
        {"title": "sql", "type": "Languages and Databases"},
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

  return jsonify(
        {"img":url_for('static', filename='images/me.JPG', _external=True),"bio": "Hi, I'm Madison! A full-stack software engineer and a recent alumni of The Marcy Lab School! I am a Hispanic, Non-Binary person from the Bronx, and I love using technology to express myself! So I'd like to use this of my portfolio as a representation of me and my personality. \n\nFirstly, I will be showing off my technical competencies and what I have experience in! Next, I have a page showing my adobe illustrator projects and my youtube channel. adobe illustrator is design software tool mostly used by graphic designers; but I decided to give it my own purpose and started creating art from my favorite animes/games! Lastly I have some of my most recent technical projects that I would like to share :) \n\nHave a nice day!!!"}
    )
