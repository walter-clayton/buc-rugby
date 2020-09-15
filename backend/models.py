# from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from models import *

class Test(db.Model):
    __tablename__ = 'test'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    firstName = db.Column(String(50), nullable=False)
    lastName = db.Column(String(50), nullable=False)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return '<id {}>'.format(self.id)