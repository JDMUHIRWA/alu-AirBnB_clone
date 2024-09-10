#!/usr/bin/python3
"""
This module defines a BaseModel class that
includes all common attributes/methods for model classes.
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """
    This is the base model class.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically containing
                      instance attributes like 'created_at' and 'updated_at'.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute `updated_at`
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object, including
                  its class name and datetime attributes in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                value = value.isoformat()
            obj_dict[key] = value

        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel class.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
