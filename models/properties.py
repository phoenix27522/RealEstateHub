#!/usr/bin/python3
from sqlalchemy import Column, LargeBinary, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base import BaseModel, Base  # Assuming BaseModel and Base are defined in models.base module

# Define the association table with extend_existing=True
properties_amenity_table = Table(
    'properties_amenity', Base.metadata,
    Column('property_id', String(60), ForeignKey('properties.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
    extend_existing=True
)

class Property(BaseModel, Base):
    """Representation of a property"""
    __tablename__ = "properties"
    __table_args__ = {'extend_existing': True}
   
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    price = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    image= Column(LargeBinary, nullable=True)

    reviews = relationship("Review", backref="property", cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", secondary=properties_amenity_table, viewonly=False)

    def __init__(self, *args, **kwargs):
        """Initializes Property"""
        super().__init__(*args, **kwargs)
