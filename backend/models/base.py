#!/usr/bin/python3
""" creating base model for all to inherit"""
import backend
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid

Base = declarative_base()

class BaseModel:
    """Base class for all models"""
    __abstract__ = True

    id = Column(String(36), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = str(uuid.uuid4())
        if 'created_at' in kwargs:
            self.created_at = self._parse_datetime(kwargs['created_at'])
        if 'updated_at' in kwargs:
            self.updated_at = self._parse_datetime(kwargs['updated_at'])

    @staticmethod
    def _parse_datetime(value):
        """Parse datetime from string representation"""
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            except ValueError:
                # Handle invalid datetime format gracefully
                return None
        return None

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"

    def save(self, session):
        """Save the instance to the database"""
        self.updated_at = datetime.utcnow()
        session.add(self)
        session.commit()

    def to_dict(self, save_fs=None, time="%Y-%m-%d %H:%M:%S"):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()  # Copy instance dictionary

        # Convert datetime attributes to strings
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)

        # Add class name to the dictionary
        new_dict["__class__"] = self.__class__.__name__

        # Remove SQLAlchemy state attribute if present
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        # Remove password if save_fs is not provided
        if save_fs is None and "password" in new_dict:
            del new_dict["password"]

        return new_dict
    
    def delete(self, session):
        """delet current instance"""
        session.delete(self)
        session.commit()
 