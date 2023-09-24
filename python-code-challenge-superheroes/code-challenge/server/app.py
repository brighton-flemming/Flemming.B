#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_migrate import Migrate

from models import db, Hero, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

heroes = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

powers = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return f"<h1>Welcome to my Flask Superhero Application</h1>"

@app.route('/heroes', methods=['GET'])
def get_heroes():
    return jsonify(heroes)

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = next((hero for hero in heroes if Hero.id == hero_id), None)

    if hero is not None:
        return jsonify(hero)
    else:
        return jsonify({"error": "Hero Not Found"}), 404
    
@app.route('/powers', methods=['GET'])
def get_powers():
    return jsonify(powers)

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = next((power for power in powers if Power.id == power_id), None)
    if power is not None:
        return jsonify(power)
    else:
        return jsonify({"error":"Power not Found"}), 404
    

@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    updated_description = request.json.get('description')

    power = next((power for power in powers if Power.id  == power_id), None)

    if power is not None:
        if updated_description is not None:
            power.description = updated_description

            return jsonify(power)
        else:
            return jsonify({"error":["Validation Errors"]}), 400
    else:
        return jsonify({"error":"Power Not Found"}), 404
    
def is_valid_strength(strength):
    valid_strengths = ['Strong', 'Weak', 'Average']
    return strength in valid_strengths
    
@app.route('/hero_powers', methods=['POST'])
def add_hero_power():
    hero_power_data = request.json
    strength = hero_power_data.get('strength')
    power_id = hero_power_data.get('power_id')
    hero_id = hero_power_data.get('hero_id')

    if not is_valid_strength(strength):
        return jsonify({"errors": ["Validation Errors"]}), 400
    
    hero = next((hero for hero in heroes if Hero.id  == hero_id), None)
    
    power = next((power for power in powers if Power.id  == power_id), None)

    if hero is not None and power is not None:

        hero_power = {
            "strength": strength,
            "power_id":power_id,
            "hero_id":hero_id,
        }

        hero.powers.append(hero_power)

        return jsonify(hero)
    else:
        return jsonify({"errors": ["Validation Errors"]}), 400

    

    


    





if __name__ == '__main__':
    app.run(port=5555, debug=True)
