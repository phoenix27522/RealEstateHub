from models.storage.REH_db import RealEstateHub_db
from models.user import User
from models.state import State
from models.properties import Property
from models.review import Review
from models.amenity import Amenity

# Instantiate the database class
db = RealEstateHub_db()

# Create a session
session = db.reload()

try:
    # Create a user
    user = User(email="titi@example.com", username="titi_user", password="13467982")
    db.new(user)
    print("User data before insertion:", user.to_dict())

    # Create a state if it doesn't exist
    state_id = "MT"
    state = db.get(State, state_id)
    if state is None:
        state = State(name="Monterial", id=state_id)
        db.new(state)
        print("State data before insertion:", state.to_dict())

    # Create a property
    property_args = {
        'city_id': 'ASM',
        'user_id': user.id,
        'name': 'Villa',
        'description': 'Beautiful apartment with stunning views',
        'number_rooms': 4,
        'number_bathrooms': 2,
        'price': 500,
        'latitude': 40.7128,
        'longitude': -74.0060
    }
    property_obj = Property(**property_args)
    db.new(property_obj)
    print("Property data before insertion:", property_obj.to_dict())

    # Create a review
    review_args = {
        'property_id': property_obj.id,  # Set the property_id
        'user_id': user.id,
        'text': 'This property is amazing!'
    }
    review_obj = Review(**review_args)
    db.new(review_obj)
    print("Review data before insertion:", review_obj.to_dict())


    # Create an amenity
    amenity_args = {
        'name': 'Swimming Pool'
    }
    amenity_obj = Amenity(**amenity_args)
    db.new(amenity_obj)
    print("Amenity data before insertion:", amenity_obj.to_dict())

    # Commit the changes to the database
    db.save()

except Exception as e:
    print(f"An error occurred: {e}")
    if session:
        session.rollback()

finally:
    # Close the session
    db.close()
