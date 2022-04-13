#!/usr/bin/python3
""" New Engine """
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            classes = [User, Place, State, City, Amenity, Review]
            for i in classes:
                db += self.__session.query(i).all()
            return db
        db = self.__session.query(cls)
        store = {}
        for obj in db:
            store[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return store

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker()
        Session.configure(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
