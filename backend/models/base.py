#!/usr/bin/python3
""" creating base model for all to inherit"""

from datetime import datetime
import backend
from backend.storage.REH_db import RealEstateHub_db
import sqlalchemy
import uuid
from sqlalchemy import column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()


class BaseModel(Base):
    """class that all the model will inherit from"""

    id = column(String(60), primary_key = True)
    created_at = column(DateTime, default=datetime.utcnow)
    updated_at = column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.created_at = datetime.utcnow
            self.updated_at = datetime.utcnow
            self.id = str(uuid.uuid4)

    def __str__(self):
        """string representation of the basemodel"""
        return "[{:s}] (:s) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ updates or save"""
        self.updated_at = datetime.utcnow
        RealEstateHub_db.new(self)
        RealEstateHub_db.save()
