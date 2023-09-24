from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String)

    powers = db.relationship('Power',secondary='hero_power', backref='hero')

class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), primary_key=True)

    heroes_power = db.relationship('Hero', backref='hero')
    powers_of_heroes = db.relationship('Power', backref='power') 

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    powers = db.relationship('Hero', secondary='hero_power', backref='power')


    

