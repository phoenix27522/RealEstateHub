#!/usr/bin/python3
""" creating base model for all to inherit"""

import database
import sqlalchemy
import uuid
from sqlalchemy import column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()
