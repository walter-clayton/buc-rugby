from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

db = SQLAlchemy()

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