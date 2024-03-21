#!/usr/bin/python3
"""db for RealEstateHub"""
import sqlalchemy
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from backend.models.base import Base


class RealEstateHub_db:
    __engine = None

    def __init__(self):
        """Instantiate a RealEstateHub object"""
        user = getenv('DB_USER')
        password = getenv('DB_PASSWORD')
        host = getenv('DB_HOST')
        name = getenv('DB_NAME')
        self.env = getenv('DB_ENV')

        try:
            self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{name}')
            if self.env == "test":
                Base.metadata.drop_all(self.__engine)

            self.session_factory = sessionmaker(bind=self.__engine)
            self.Session = scoped_session(self.session_factory)
        except SQLAlchemyError as e:
            print(f"Error connecting to the database: {e}")
            raise

    def get_session(self):
        """Get a database session."""
        return self.Session()

    def close_session(self):
        """Close the database session."""
        self.Session.remove()

    def create_all(self):
        """Create all tables."""
        Base.metadata.create_all(self.__engine)

    def drop_all(self):
        """Drop all tables."""
        Base.metadata.drop_all(self.__engine)