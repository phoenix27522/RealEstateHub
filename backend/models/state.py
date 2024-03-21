#!/usr/bin/python3

from backend.models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class State(BaseModel, Base):
    """Representation of state"""
    __tablename__ = "state"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)