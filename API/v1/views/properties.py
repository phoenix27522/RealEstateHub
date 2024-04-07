#!/usr/bin/python3
""" objects that handle all default RestFul API actions for properties """
import logging
from models.state import State
from models.city import City
from models.properties import Property
from models.user import User
from models.amenity import Amenity
from models import storage
from API.v1.views import app_views
from flask import abort, jsonify, make_response, request
from sqlalchemy.orm import joinedload
from flasgger.utils import swag_from

logging.basicConfig(level=logging.DEBUG)

@app_views.route('/cities/<city_id>/properties', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/property/get_propertys.yml', methods=['GET'])
def get_propertys(city_id):
    """
    Retrieves the list of all Property objects of a City
    """
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    properties = [property.to_dict() for property in city.properties]

    return jsonify(properties)


@app_views.route('/properties/<property_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/property/get_property.yml', methods=['GET'])
def get_property(property_id):
    """
    Retrieves a Property object
    """
    property = storage.get(Property, property_id)
    if not property:
        abort(404)

    # Eager load the amenities associated with the property
    property = storage.db_session.query(Property).options(joinedload('amenities'), joinedload('city'), joinedload('city.state')).filter_by(id=property_id).one()


    return jsonify(property.to_dict())


@app_views.route('/properties/<property_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/property/delete_property.yml', methods=['DELETE'])
def delete_property(property_id):
    """
    Deletes a Property Object
    """

    property = storage.get(Property, property_id)

    if not property:
        abort(404)

    storage.delete(property)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/properties', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/property/post_property.yml', methods=['POST'])
def post_property(city_id):
    """
    Creates a Property
    """
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])

    if not user:
        abort(404)

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data["city_id"] = city_id
    instance = Property(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/properties/<property_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/property/put_property.yml', methods=['PUT'])
def put_property(property_id):
    """
    Updates a Property
    """
    property = storage.get(Property, property_id)

    if not property:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(property, key, value)
    storage.save()
    return make_response(jsonify(property.to_dict()), 200)


@app_views.route('/propertys_search', methods=['POST'], strict_slashes=False)
@swag_from('documentation/property/post_search.yml', methods=['POST'])
def propertys_search():
    """
    Retrieves all Property objects depending on the JSON in the body
    of the request
    """
    logging.debug("Received request to search for properties")

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    logging.debug("Received JSON data: %s", data)

    if data and len(data):
        states = data.get('states', None)
        cities = data.get('cities', None)
        amenities = data.get('amenities', None)

    if not data or not len(data) or (
            not states and
            not cities and
            not amenities):
        properties = storage.all(Property).values()
        list_properties = []
        for property in properties:
            list_properties.append(property.to_dict())
        return jsonify(list_properties)

    list_properties = []
    if states:
        states_obj = [storage.get(State, s_id) for s_id in states]
        for state in states_obj:
            if state:
                for city in state.cities:
                    if city:
                        for property in city.properties:
                            list_properties.append(property)

    if cities:
        city_obj = [storage.get(City, c_id) for c_id in cities]
        for city in city_obj:
            if city:
                for property in city.properties:
                    if property not in list_properties:
                        list_properties.append(property)

    if amenities:
        # Fetch all properties if list_properties is empty
        if not list_properties:
            list_properties = storage.all(Property).values()
        # Filter properties based on amenities
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_properties = [property for property in list_properties
                           if all([am in property.amenities
                                   for am in amenities_obj])]

    properties = []
    for p in list_properties:
        d = p.to_dict()
        d.pop('amenities', None)
        properties.append(d)

    return jsonify(properties)

