#!usr/bin/python3
"""This is a test module for the base_model

"""


from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """class for creation of tests for base_model module

    """
    def test_attributes(self):
        """ Test the attributes in different cases

        """
        inst_1 = BaseModel()
        # test if id is string
        self.assertIsInstance(inst_1.id, str)
        inst_2 = BaseModel()
        # test different id
        self.assertNotEqual(inst_1.id, inst_2.id)
        # test if created_at is datetime
        self.assertIsInstance(inst_1.created_at, datetime)
        # test if update_at is datetime
        self.assertIsInstance(inst_1.updated_at, datetime)

    def test_save(self):
        """ Testing the save method

        """
        inst_1 = BaseModel()
        # test the updated_at before and after save()
        first_updated_at = inst_1.updated_at
        inst_1.save()
        second_updated_at = inst_1.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)
        # test the type of updated_at after save()
        self.assertIsInstance(inst_1.updated_at, datetime)

    def test_to_dict(self):
        """ Test to_dict method.
        """
        inst_1 = BaseModel()
        dict_1 = inst_1.to_dict()
        # Test type dict
        self.assertIsInstance(dict_1, dict)
        # test if dictionary updates automatically
        inst_1.save()
        dict_2 = inst_1.to_dict()
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])

if __name__ == '__main__':
    unittest.main()
