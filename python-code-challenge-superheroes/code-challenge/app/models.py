from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String)

    powers = db.relationship('Power',secondary='hero_power' back_populates='heroes')

class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), primary_key=True)

    hero = db.relationship('Hero', back_populates='heroes')
    power = db.relationship('Power', back_populates='powers') 

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    heroes = db.relationship('Hero', secondary='hero_power', back_populates='powers')


    

# add any models you may need. 