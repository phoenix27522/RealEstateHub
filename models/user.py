#!/usr/bin/python3
"""creats the user class that inherit from the base"""
from models.base import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    username = Column(String(128), nullable=True)
    properties = relationship("Property", backref="user")
    reviews = relationship("Review", backref="user")

    def __init__(self, *args, **kwargs):
        """Initializes the user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
