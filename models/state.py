#!/usr/bin/python3

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Representation of state"""
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True} 
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                            backref="state",
                            cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)