#!/usr/bin/python3
""" Index """
from models.amenity import Amenity
from models.city import City
from models.properties import Property
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from API.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Property, Review, State, User]
    names = ["amenities", "cities", "properties", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
