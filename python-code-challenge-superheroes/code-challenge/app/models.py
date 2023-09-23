from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String)

    powers = db.relationship('Power',secondary='hero_power' backref='heroes')


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)

    heroes = db.relationship('Hero', backref='powers')


    

# add any models you may need. 