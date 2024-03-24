from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import Session


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

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{name}')

        if self.env == "test":
            Base.metadata.drop_all(self.__engine)

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
        """Reloads data from the database"""
        if self.__session:
            self.close()  # Close existing session
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sess_factory)
        self.__session = session()


    def close(self):
        try:
            if self.__session:
                self.__session.close()
                self.__session = None  # Reset session to None after closing
            else:
                print("Session is already closed or not initialized.")
        except Exception as e:
            print(f"An error occurred while closing the session: {str(e)}")

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        return self.__session.query(cls).filter_by(id=id).first()
