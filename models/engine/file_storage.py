#!/usr/bin/python3
"""
This module contains the methods for serialization/deserialization
and also save the data in files.
"""


import json
from models.base_model import BaseModel

class FileStorage():
    """this class serializes json to a file and
    deserializes from a file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """set the __objects with obj in the key
        <obj class name>.id

        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to a JSON path from __file_path

        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
            #mucha discusión por acá si va el self o no

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Deserialize the JSON file to __objects (only if JSON file exists).

        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                all_dicts = json.load(f)
            for key, value in all_dicts.items():
                # Loop through dictionary of dictionaries,
                # Creating an instance of the class for each dictionary.
                inst = value.__class__(value)
                # Save new instance in __objects.
                self.new(inst)
        except:
            pass
