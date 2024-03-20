#!/usr/bin/python3
"""db for RealEstateHub"""
import sqlalchemy
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from backend.models.base import Base


class RealEstateHub_db:
    __engine = None

    def __init__(self):
        """Instantiate a RealEstateHub object"""
        user = getenv('DB_USER')
        password = getenv('DB_PASSWORD')
        host = getenv('DB_HOST')
        db = getenv('DB_NAME')
        env = getenv('DB_ENV')

        if user is None or password is None or host is None or db is None:
            raise ValueError("Database configuration environment variables are not set.")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}')
        if env == "test":
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.session = Session()

    