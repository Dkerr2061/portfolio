#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Local imports
from app import app
from config import bcrypt
from models import db, Project, User

if __name__ == '__main__':
   
    with app.app_context():
        User.query.delete()
        Project.query.delete()

        user1 = User(username='dkerr', password_hash='dkerr123')

        project1 = Project(name='Webflix', link='https://github.com/Dkerr2061/webflix.git', description='My first fullstack project', image='', rating=9.8)

        db.session.add_all([user1])
        db.session.add_all([project1])
        db.session.commit()


        print("🌱 Database successfully seeded! 🌱")