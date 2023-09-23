
from random import randint, choice

from app.app import db
from app.models import Hero, HeroPower, Power


def SeedingPowers():
    message = print("🦸‍♀️ Seeding powers...")
    return f"<h2>{ message }</h2>"

powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

for power_info in powers_data:
    power = Power(**power_info)
    db.session.add(power)

    db.session.commit()

    def SeedingPowersDone():
        message = print("🦸‍♀️ Seeding powers... Done!")
        return f"<h2>{ message }</h2>"

def SeedingHeroes():
    message = print("🦸‍♀️ Seeding heroes...")
    return f"<h2>{ message }</h2>"

heroes_data = [
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

for hero_info in heroes_data:
    hero = Hero(**hero_info)
    db.session.add(hero)

db.session.commit()

def SeedingHeroesDone():
    message = print("🦸‍♀️ Seeding heroes...Done!")
    return f"<h2>{ message }</h2>"

def AddingPowers():
    message = print("🦸‍♀️ Adding powers to heroes...")
    return f"<h2>{ message }</h2>"

strengths = ["Strong", "Weak", "Average"]

for hero in Hero.query,all():
    for _ in range(randint(1,3)):
        power = Power.query.get(randint(1, len(powers_data)))
        strength = choice(strengths)

        hero_power = HeroPower(hero=hero, power=power, strength=strength)
        db.session.add(hero_power)

db.session.commit()

def SeedingComplete():
    message = print("🦸‍♀️ Done seeding!")
    return f"<h2>{ message }</h2>"





