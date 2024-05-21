from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False, unique=True)
  password_hash = db.Column(db.String, nullable=False)

class Project(db.Model, SerializerMixin):
  __tablename__ = 'projects'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  link = db.Column(db.String, nullable=False)
  description = db.Column(db.String, nullable=False)
  image = db.Column(db.String)
  rating = db.Column(db.Float)