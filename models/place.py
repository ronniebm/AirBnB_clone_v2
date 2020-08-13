#!/usr/bin/python3
"""Place Module for HBNB project."""
from models.base_model import BaseModel, Base
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship
import models
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        reviews = relationship('Review', backref='place',
                               cascade="all, delete")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='place_amenities', viewonly=False)
    else:

        @property
        def reviews(self):
            """Funtion for returns a list of review."""
            review_list = []
            review_dict = models.storage.all(Review)
            for key, value in review_dict.items():
                review_list.append(review_dict[key])
            return review_list

        @property
        def amenities(self):
            """Funtion for returns a list of amenities ids."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """Setter method for add id to amenity_ids."""
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj)
