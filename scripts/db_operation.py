#!/usr/bin/python3
from backend.storage.REH_db import RealEstateHub_db  # Import your database class
from backend.models.user import User  # Import the User model
from backend.models.properties import Properties  # Import the Properties model
from backend.models.city import City  # Import the City model
from backend.models.state import State  # Import the State model
from backend.models.review import Review  # Import the Review model
from backend.models.amenity import Amenity  # Import the Amenity model

# Instantiate the database class
db = RealEstateHub_db()

# Create all tables (if they don't exist)
db.create_all()

# Get a session from the database
session = db.get_session()

try:
    # Create a user
    user = User(email="adiam@example.com", username="fruth_user", password="123456789")
    session.add(user)

    # Create a property
    property_1 = Properties(
        user_id=user.id,
        name="Sample Property",
        description="This is a sample property",
        number_rooms=3,
        number_bathrooms=2,
        price=200000,
        latitude=123.456,
        longitude=456.789
    )
    session.add(property_1)

    # Create a city
    city = City(name="New York", state_id="NY")
    session.add(city)

    # Create a state
    state = State(name="New York")
    session.add(state)

    # Create a review
    review = Review(user_id=user.id, properties_id=property_1.id, text="This property is great!")
    session.add(review)

    # Create an amenity
    amenity = Amenity(name="Swimming Pool")
    session.add(amenity)

    # Commit the changes to the database
    session.commit()

except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()

finally:
    # Close the session
    db.close_session()

