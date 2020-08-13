#!/usr/bin/python3
"""Place Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
import models


class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__ = 'places'
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
    reviews = relationship('Review', backref='pace', cascade="all, delete")

    @property
    def reviews(self):
        """returns a list of review instances with place_id"""
        review_list = []
        review_dict = models.storage.all(Review)
        for key, value in review_dict.items():
            review_list.append(review_dict[key])
        return review_list

    @property
    def amenities(self):
        """Returns the list of Amenity instances
        based on the attribute amenity_ids
        """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """Add id to amenity_ids."""
        for key, value in models.storage.all(Amenity):
            if value.amenity_id == amenity.id:
                self.amenity_ids.append(value)
