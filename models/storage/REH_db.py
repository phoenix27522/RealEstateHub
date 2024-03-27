import logging
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base import Base
from models.amenity import Amenity
from models.city import City
from models.properties import Property
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Property": Property, "Review": Review, "State": State, "User": User}

class RealEstateHub_db:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a RealEstateHub object"""
        user = getenv('DB_USER')
        password = getenv('DB_PASSWORD')
        host = getenv('DB_HOST')
        name = getenv('DB_NAME')
        self.env = getenv('DB_ENV')

        if None in {user, password, host, name}:
            raise ValueError("Database environment variables not properly set")

        logging.info(f"Connecting to database {name} on {host}...")
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{name}')

        if self.env == "test":
            logging.info("Dropping existing tables for test environment...")
            Base.metadata.drop_all(self.__engine)

        self.reload()

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = [obj for cls in classes.values() for obj in self.__session.query(cls).all()]
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        logging.info("Reloading session...")
        # Close existing session if it exists
        self.close()

        # Create all tables
        Base.metadata.create_all(self.__engine)

        # Create a new session
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess_factory)
        self.__session()

        logging.info("Session reloaded successfully.")



    def close(self):
        try:
            if self.__session:
                self.__session.close()
                logging.info("Session closed successfully.")
            else:
                logging.warning("Session is already closed or not initialized.")
        except Exception as e:
            logging.error(f"An error occurred while closing the session: {str(e)}")

    
    def get_session(self):
        """Returns the current session."""
        return self.__session

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        return self.__session.query(cls).filter_by(id=id).first()

logging.basicConfig(level=logging.INFO)
db = RealEstateHub_db()
