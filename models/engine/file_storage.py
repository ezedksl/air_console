#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes

"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects

        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        """
        key = "{}.{}".format(type(obj), obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        objects = dict(FileStorage.__objects)
        serialObj = {}
        for key in objects:
            serialObj[key] = json.dumps(key)

        with open(FileStorage.__file_path, 'w') as jsfile:
            json.dump(serialObj, jsfile)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'w') as jsfile:
                json.load(jsfile)
        except:
            pass
