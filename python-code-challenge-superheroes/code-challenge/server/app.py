#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_migrate import Migrate


from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)



@app.route('/')
def home():
    return f"<h1>Welcome to my Flask Superhero Application</h1>"

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_list = [{'id':hero.id, 'name': hero.name, 'super_name':hero.super_name}for hero in heroes]
    return jsonify(hero_list)

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)

    if hero is not None:
        return jsonify({'id':hero.id, 'name': hero.name, 'super_name':hero.super_name})
    else:
        return jsonify({"error": "Hero Not Found"}), 404

    
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_list = [{'id':power.id, 'name': power.name, 'description':power.description} for power in powers]
    return jsonify(power_list)

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)

    if power is not None:
        return jsonify({'id':power.id, 'name': power.name, 'description':power.description})
    else:
        return jsonify({"error":"Power not Found"}), 404
    

@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)

    if not power :
         return jsonify({"error":"Power Not Found"}), 404
    data = request.json
    updated_description = data.get('description')

    if updated_description is not None:
            power.description = updated_description
            db.session.commit()
            return jsonify({"message":"Power updated successfully"})
    else:
            return jsonify({"error":["Description is required"]}), 400
       
    
def is_valid_strength(strength):
    valid_strengths = ['Strong', 'Weak', 'Average']
    return strength in valid_strengths
    
@app.route('/hero_powers/<int:hero_id>', methods=['POST'])
def add_hero_power(hero_id):

    hero = Hero.query.get(hero_id)

    if not hero:
        return jsonify({"error": "Hero Not Found"})
    
    data = request.json
    strength = data.get('strength')
    power_id = data.get('power_id')

    if not strength or not power_id:
        return jsonify({"error": "Strength and power_id are required"})
    
    power = Power.query.query.get(power_id)

    if not power:
         return jsonify({"error":"Power Not Found"})
    
    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    db.session.add(hero_power)
    db.commit()

    return jsonify({"message":"Hero Power added successfully."})



    

if __name__ == '__main__':
    app.run(port=3000, debug=True)
