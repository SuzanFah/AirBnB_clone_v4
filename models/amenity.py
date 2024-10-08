#!/usr/bin/python3
"""
Contains the Amenity class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """Represents an amenity for a place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
