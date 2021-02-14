#!/usr/bin/python3
""" This is the module for testing of the file_storage module

"""
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from os import path


class TestFileStorage(unittest.TestCase):
    """ Class for the creation of tests for the file_storage module

    """
    # Test creation of new objects
    def test_objects(self):
        """ Test....
        
        """
        inst1 = BaseModel()
        inst1.save()
        # Check if file is created
        self.assertTrue(path.exists('file.json'))
        # Check if file is not empyty
        self.assertTrue(path.getsize('file.json') > 0)
        # Test the all() method through the storage in INIT
        objects = storage.all() # In this case this shouldn't be empty        
        self.assertTrue(len(objects) > 0)
