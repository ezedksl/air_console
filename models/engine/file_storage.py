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
    __objects: {}

    def all(self):
        """return the __objects dictionary
        """
        return self.__objects

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
            #mucha discusión por acá

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

"""{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d":
    {"my_number": 89, "__class__":"BaseModel",
     "updated_at": "2017-09-28T21:07:25.047381",
     "created_at": "2017-09-28T21:07:25.047372",
     "name": "Holberton",
     "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}"""

    def reload(self):
        """ Deserialize the JSON file to __objects (only if JSON file exists).

        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                all_dicts = json.load(f)
            for key, value in all_dicts.items():
                # Loop through dictionary of dictionaries,
                # Creating an
                inst = value.__class__(value)
                self.new(inst)
        except:
            pass
