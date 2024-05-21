#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
# from config import app, db, api, bcrypt
from config import *
# Add your model imports
from models import User, Project