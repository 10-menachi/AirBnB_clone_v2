#!/usr/bin/python3

"""
This module defines a class to manage database storage for hbnb clone
"""


class DBStorage:
    """
    This class manages storage of hbnb models in a database
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new DBStorage instance
        """
        from models.base_model import Base
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from os import getenv

        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        objs = {}
        if cls is not None:
            for k, v in self.__session.query(classes[cls]).all():
                objs[k] = v
        else:
            for c in classes.values():
                for k, v in self.__session.query(c).all():
                    objs[k] = v
        return objs

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves storage dictionary to file
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads objects from database
        """
        from models.base_model import Base
        from sqlalchemy.orm import sessionmaker, scoped_session
        from sqlalchemy.orm import scoped_session

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(Session)

    def close(self):
        """
        Calls remove method on the private session attribute
        """
        self.__session.remove()
