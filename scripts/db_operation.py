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
    user1 = User(email="senait@example.com", username="senait", password="password6")
    db.new(user1)
    print("User data before insertion:", user1.to_dict())

    user2 = User(email="titi@example.com", username="titi", password="password8")
    db.new(user2)
    print("User data before insertion:", user2.to_dict())

    # Create a state if it doesn't exist
    state_id = "KMPL"
    state = db.get(State, state_id)
    if state is None:
        state = State(name="kampala", id=state_id)
        db.new(state)
        print("State data before insertion:", state.to_dict())

    # Create a city in Uganda
    city_id = "MKYD"
    city = db.get(City, city_id)
    if city is None:
        city = City(name="makindye", id=city_id, state_id=state_id)
        db.new(city)
        print("City data before insertion:", city.to_dict())

    # Create properties for different users
    property1_args = {
        'city_id': city_id,
        'user_id': user1.id,
        'name': 'Apartment',
        'description': 'perfect for family in the heart of Kampala',
        'number_rooms': 2,
        'number_bathrooms': 1,
        'price': 300,
        'latitude': 0.3476,
        'longitude': 32.5825,
        'image_path':'../static/images/apartment1.jpg'
    }
    property1 = Property(**property1_args)
    db.new(property1)
    print("Property data before insertion:", property1.to_dict())

    property2_args = {
        'city_id': city_id,
        'user_id': user2.id,
        'name': 'Villa',
        'description': 'Luxurious Apartement with a scenic view',
        'number_rooms': 6,
        'number_bathrooms': 3,
        'price': 1000,
        'latitude': 0.3151,
        'longitude': 32.5811,
        'image_path': '../static/images/villa1.jpeg'

    }
    property2 = Property(**property2_args)
    db.new(property2)
    print("Property data before insertion:", property2.to_dict())

    # Create reviews for properties
    review1_args = {
        'property_id': property1.id,
        'user_id': user2.id,
        'text': 'Great place to rise family!'
    }
    review1 = Review(**review1_args)
    db.new(review1)
    print("Review data before insertion:", review1.to_dict())

    review2_args = {
        'property_id': property2.id,
        'user_id': user1.id,
        'text': 'what a view!'
    }
    review2 = Review(**review2_args)
    db.new(review2)
    print("Review data before insertion:", review2.to_dict())

    # Check if the Amenity "pet" exists, otherwise create it
    amenity_pet = db.get(Amenity, 'gym')
    if amenity_pet is None:
        amenity_pet_args = {
            'name': 'gym',
            'id': 'gym'
        }
        amenity_pet = Amenity(**amenity_pet_args)
        db.new(amenity_pet)
        print("Amenity data before insertion:", amenity_pet.to_dict())

    # Associate Amenity "pet" with specific properties
    property1.amenities.append(amenity_pet)
    property2.amenities.append(amenity_pet)

    # Commit the changes to the database
    db.save()

except Exception as e:
    print(f"An error occurred: {e}")
    if session:
        session.rollback()

finally:
    # Close the session
    db.close()
