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
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return f"{self.firstName}:{self.lastName}"