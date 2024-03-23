import models
from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Amenity(BaseModel, Base):
    """Representation of review"""
    __tablename__ = 'amenities'
    __table_args__ = {'extend_existing': True} 
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)