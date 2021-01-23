from datetime import datetime
# from flaskblog import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from flask_migrate import Migrate, MigrateCommand
# from models import db, InfoModel
from psycopg2 import connect, Error
from psycopg2.extras import Json
from psycopg2.extras import json as psycop_json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.username}, {self.email}, {self.image_file}"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class InfoModel(db.Model):
    __tablename__ = 'info_table'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    bodyFat = db.Column(db.String(50), nullable=False)
    bodyMass = db.Column(db.String(50), nullable=False)
    height = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    tenSprint = db.Column(db.String(50), nullable=False)
    thirtySprint = db.Column(db.String(50), nullable=False)
    twentySprint = db.Column(db.String(50), nullable=False)

    def __init__(self, id, firstName, lastName, bodyFat, bodyMass, height, position, tenSprint, thirtySprint, twentySprint):
        self.id = id
        self.date = date
        self.firstName = firstName
        self.lastName = lastName
        self.bodyFat = bodyFat
        self.bodyMass = bodyMass
        self.height = height
        self.position = position
        self.tenSprint = tenSprint
        self.thirtySprint = thirtySprint
        self.twentySprint = twentySprint
        
    def __repr__(self):
        return f"{self.firstName}:{self.lastName}:{self.bodyFat}:{self.bodyMass}:{self.height}:{self.tenSprint}:{self.thirtySprint}:{self.twentySprint}"