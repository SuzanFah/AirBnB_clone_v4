#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import uuid
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Check storage type directly from environment variable
storage_t = getenv("HBNB_TYPE_STORAGE")

# Conditional base class assignment
if storage_t == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    # Define the columns only if using the database storage
    if storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

        # Handle initialization from kwargs
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

