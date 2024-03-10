#!/usr/bin/python3
"""this class handles file storage"""


import json

class FileStorage:
    """helps with storing files using JSON
    Attributes:
        __file_path (string) - path to the JSON file e.g. file.json
        __objects (dict) - will store all objects by <class name>.id
            e.g. BaseModel.1212
    """
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj classname>.id"""
        ky = obj.__class__.__name__ + str(obj.id)
        FileStorage.__objects[ky] = obj

    def save(self):
        """serialises __objects to the JSON file (path: __file_path"""
        enc = "utf-8"
        fpath = FileStorage.__file_path
        with open(fpath, "a", encoding = "utf-8") as fname:
            for key, obj in FileStorage.__objects.items():
                json.dump(obj, fname)

    def reload(self):
        """deserialises the JSON file to __objects only if the JSON file
        __file_path exists. otherwise, do nothing don't even raise exceptions"""
        try:
            fpath = FileStorage.__file_path
            with open(fpath, "r", encoding = "utf-8") as fname:
                obj = json.load(fname)
                name = obj.__class__.__name__ + obj.id
                FileStorage.__objects[name] = obj
        except FileNotFoundError:
            pass
