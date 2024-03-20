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
        user = getenv('admin')
        password = getenv('nk0701540135')# find if there is way not to hard code the paaword to db
        host = getenv('localhost') # change it to DNS(only for testing and deploying)
        db = getenv('db_RealEstateHub')
        env = getenv('db_env')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db))
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    