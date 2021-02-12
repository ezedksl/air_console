#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes

"""


import datetime
import uuid


class BaseModel():
    """Base class for the console

    """
    def __init__(self):
        """instance initiation method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns the print() and str() representation

        """
        return ("[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """saves the instance and updated the updated_at time"""
        self.updated_at = datetime.datetime

    def to_dict(self):
        """return the dictionary of the instance"""
        inst_dict = self.__dict__
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
