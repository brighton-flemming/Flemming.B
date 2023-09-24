from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    super_name = db.Column(db.String(255))

    powers = db.relationship('Power',secondary='hero_power', backref='hero')
    heroes_power = db.relationship('HeroPower', backref ='hero')

class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20))
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), primary_key=True)

    heroes_power = db.relationship('Hero', backref='hero_powers')
    powers_of_heroes = db.relationship('Power', backref='hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'")
        return value 

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(500))

    powers = db.relationship('Hero', secondary='hero_power', backref='power')
    powers_of_heroes = db.relationship('HeroPower', backref='power') 

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < value:
            raise ValueError("Description has to be at least 20 characters long.")
        return value


    

