#!/usr/bin/python3
"""The base model, from which all other classes will inherit.
"""

import cmd
from datetime import datetime
import json
import uuid
from __init__ import storage


class BaseModel:
    """the Base Model class.
        It defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """the initialiser
        self.id should assign a uuid4 from uuid module
        """
        if (kwargs):
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        val = datetime.strptime(val, fmt)
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """print the base in printable format"""
        cls_name = self.__class__.__name__
        my_id = self.id
        my_dct = self.__dict__
        return "[{}] ({}) {}".format(cls_name, my_id, my_dct)


    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dct = {}
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
