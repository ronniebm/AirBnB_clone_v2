#!/usr/bin/python3
"""Amenity module for the HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# from models.place import place_amenity
from os import getenv


class Amenity(BaseModel, Base):
    """Review classto store review information."""

    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""
