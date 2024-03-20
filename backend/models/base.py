#!/usr/bin/python3
""" creating base model for all to inherit"""

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

