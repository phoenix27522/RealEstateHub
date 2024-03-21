#!/usr/bin/python3

from backend.models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """Representation of review"""
    __tablename__ = "review"
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    properties_id = Column(String(128), ForeignKey('properties.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)