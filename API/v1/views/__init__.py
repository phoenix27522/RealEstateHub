#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/API/v1')

from API.v1.views.index import *
from API.v1.views.states import *
from API.v1.views.properties import *
from API.v1.views.properties_reviews import *
from API.v1.views.cities import *
from API.v1.views.amenities import *
from API.v1.views.users import *
from API.v1.views.properties_amenities import *
