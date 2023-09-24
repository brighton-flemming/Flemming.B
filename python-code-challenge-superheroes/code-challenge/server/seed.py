
from random import randint, choice

from app import db, app
from models import Hero, HeroPower, Power

def seed_database():

    Hero.query.delete()
    HeroPower.query.delete()
    Power.query.delete()


    def SeedingPowers():
        message = print("🦸‍♀️ Seeding powers...")
        return f"<h2>{ message }</h2>"
   
    SeedingPowers()

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
    SeedingPowersDone()

    def SeedingHeroes():
        message = print("🦸‍♀️ Seeding heroes...")
        return f"<h2>{ message }</h2>"
    SeedingHeroes()

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
    SeedingHeroesDone()

    def AddingPowers():
       message = print("🦸‍♀️ Adding powers to heroes...")
       return f"<h2>{ message }</h2>"
    AddingPowers()

    strengths = ["Strong", "Weak", "Average"]
    added_combinations = set()

    for hero in Hero.query.all():
      for _ in range(randint(1,3)):
          combination = (hero.id, power.id)
          strength = choice(strengths)

          hero_id = hero.id
          power_id = power.id

      if combination not in added_combinations:
          hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
          db.session.add(hero_power)
          added_combinations.add(combination)
          break

    db.session.commit()

    def SeedingComplete():
     message = print("🦸‍♀️ Done seeding!")
     return f"<h2>{ message }</h2>"
    SeedingComplete()


if __name__ == "__main__":
    with app.app_context():
     seed_database()





