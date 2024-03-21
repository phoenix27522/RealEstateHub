#!/usr/bin/python3
from backend.storage.REH_db import RealEstateHub_db  # Import your database class
from backend.models.user import User # Import the User model
from backend.models.properties import Properties

# Instantiate the database class
db = RealEstateHub_db()

# Create all tables (if they don't exist)
db.create_all()

# Get a session from the database
session = db.get_session()

# Create a new user
new_user = User(email='example@exampl.com', username='examle_user', password='password123')

# Save the user to the database
new_user.save(session)

# Commit the changes to the database
session.commit()

# Close the session
db.close_session()
