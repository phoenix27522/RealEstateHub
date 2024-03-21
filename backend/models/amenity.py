from backend.models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Amenity(BaseModel, Base):
    """Representation of review"""
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)