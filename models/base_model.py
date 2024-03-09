#!/usr/bin/python3
"""The base model, from which all other classes will inherit.
"""


class BaseModel:
    """the Base Model class.
        It defines all common attributes/methods for other classes
    """

    def __init__(self, obj_id, created_at, updated_at):
        """the initialiser
        self.id should assign a uuid4 from uuid module
        """
        self.id = obj_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """print the base in printable format"""
        cls_name = self.__class__.__name__
        my_id = self.id
        my_dct = self.__dict__
        print("[{}] ({}) {}".format(cls_name, my_id, my_dct))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = 0

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        return {}
