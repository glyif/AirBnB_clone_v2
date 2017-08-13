#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from os import getenv
from sqlalchemy import Column, String

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
