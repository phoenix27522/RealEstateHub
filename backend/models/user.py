#!/usr/bin/python3
"""creats the user class that inherit from the base"""
from backend.models.base import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5

class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), unique=True, nullable=False)
    username = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the user"""
        super().__init__(*args, **kwargs)

    def save(self, session):
        """Save the instance to the database"""
        # Hash the password before saving
        self.password = md5(self.password.encode()).hexdigest()
        super().save(session)
