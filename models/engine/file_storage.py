#!usr/bin/python3
"""
This module contains the methods for serialization/deserialization
and also save the data in files
"""


import json
from models.base_model import BaseModel

class FileStorage():
    """this class serializes json to a file and
    deserializes from a file
    """
    __file_path = "file.json"
    __objects: {}

    def all(self):
        """return the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """set the __objects with obj in the key
        <obj class name>.id
        """
        key = str(obj.__class__.__name__ + '.' + obj.id)
        FileStorage.__objects[key] = obj
        # setattr(FileStorage.__objects, obj.__class__.__name__.id, obj)

    def save(self):
        """serializes __objects to a JSON path from __file_path
        """
        with open(__file_path, 'w') as f:
            json.dump(__objects, f)

    def reload(self):
        """deserialize the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                __objects = json.load(f)
        except:
            pass
