from models.storage.REH_db import RealEstateHub_db
from models.user import User
from models.state import State
from models.city import City
from models.properties import Property
from models.review import Review
from models.amenity import Amenity

# Instantiate the database class
db = RealEstateHub_db()

# Create a session
session = db.reload()

try:
    # Create users
    user1 = User(email="nahom@example.com", username="nahom", password="password5")
    db.new(user1)
    print("User data before insertion:", user1.to_dict())

    user2 = User(email="adu@example.com", username="adu", password="password7")
    db.new(user2)
    print("User data before insertion:", user2.to_dict())

    # Create a state if it doesn't exist
    state_id = "UG"
    state = db.get(State, state_id)
    if state is None:
        state = State(name="Uganda", id=state_id)
        db.new(state)
        print("State data before insertion:", state.to_dict())

    # Create a city in Uganda
    city_id = "EBB"
    city = db.get(City, city_id)
    if city is None:
        city = City(name="Entebbeb", id=city_id, state_id=state_id)
        db.new(city)
        print("City data before insertion:", city.to_dict())

    # Create properties for different users
    property1_args = {
        'city_id': city_id,
        'user_id': user1.id,
        'name': 'Apartment 1',
        'description': 'perfect for family in the heart of Kampala',
        'number_rooms': 5,
        'number_bathrooms': 2,
        'price': 500,
        'latitude': 0.3476,
        'longitude': 32.5825
    }
    property1 = Property(**property1_args)
    db.new(property1)
    print("Property data before insertion:", property1.to_dict())

    property2_args = {
        'city_id': city_id,
        'user_id': user2.id,
        'name': 'Villa 1',
        'description': 'Luxurious Apartement with a scenic view',
        'number_rooms': 4,
        'number_bathrooms': 3,
        'price': 800,
        'latitude': 0.3151,
        'longitude': 32.5811
    }
    property2 = Property(**property2_args)
    db.new(property2)
    print("Property data before insertion:", property2.to_dict())

    # Create reviews for properties
    review1_args = {
        'property_id': property1.id,
        'user_id': user2.id,
        'text': 'Great place to stay!'
    }
    review1 = Review(**review1_args)
    db.new(review1)
    print("Review data before insertion:", review1.to_dict())

    review2_args = {
        'property_id': property2.id,
        'user_id': user1.id,
        'text': 'Amazing villa, highly recommended!'
    }
    review2 = Review(**review2_args)
    db.new(review2)
    print("Review data before insertion:", review2.to_dict())

    # Create amenities
    amenity1_args = {
        'name': 'pet'
    }
    amenity1 = Amenity(**amenity1_args)
    db.new(amenity1)
    print("Amenity data before insertion:", amenity1.to_dict())

    amenity2_args = {
        'name': 'Wifi'
    }
    amenity2 = Amenity(**amenity2_args)
    db.new(amenity2)
    print("Amenity data before insertion:", amenity2.to_dict())

    # Commit the changes to the database
    db.save()

except Exception as e:
    print(f"An error occurred: {e}")
    if session:
        session.rollback()

finally:
    # Close the session
    db.close()
