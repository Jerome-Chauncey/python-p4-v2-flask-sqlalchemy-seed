#!/usr/bin/env python3
#server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    #create and initialize a faker genarator
    fake = Faker()

    Pet.query.delete()

    # Create an empty list
    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)
    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()