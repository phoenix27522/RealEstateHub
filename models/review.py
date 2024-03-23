#!/usr/bin/python3

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """Representation of review"""
    __tablename__ = 'reviews'
    __table_args__ = {'extend_existing': True}
    
    property_id = Column(String(60), ForeignKey('properties.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes Review"""
        super().__init__(*args, **kwargs)

