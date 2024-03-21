#!/usr/bin/python3
from backend.models.base import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey

class Properties(BaseModel, Base):
    """repersentation of properties"""
    __tablename__ = "properties"
    user_id = Column(String(128), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=1)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    price = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)