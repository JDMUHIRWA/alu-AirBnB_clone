#!/usr/bin/python3
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test case for the BaseModel class in the 'models' module."""

    def setUp(self):
        """Set up the initial state for the tests."""
        self.obj_1 = BaseModel()
        self.obj_2 = BaseModel()

    def tearDown(self):
        """Clean up resources after each test."""
        del self.obj_1
        del self.obj_2

    def test_instantiation(self):
        """Test if BaseModel objects are instantiated correctly."""
        self.assertIsInstance(self.obj_1, BaseModel)

    def test_attr_type(self):
        """Test the data types of specific attributes of BaseModel objects."""
        with self.subTest():
            self.assertIsInstance(self.obj_1.id, str)
        with self.subTest():
            self.assertIsInstance(self.obj_1.updated_at, datetime)

    def test_unique_id(self):
        """ Test if the id attribute of different
        BaseModel instances is unique.
        """
        self.assertNotEqual(self.obj_1.id, self.obj_2.id)

    def test_id_assignment(self):
        """ validate that The id attribute of the BaseModel object is a
        valid UUID.
        """
        self.assertTrue(uuid.UUID(self.obj_1.id, version=4))

    def test_to_dict_obj(self):
        """ Test the conversion of BaseModel object attributes to a
        dictionary using to_dict() method.
        """
        self.obj_1.updated_at = datetime.utcnow()
        obj_dict = self.obj_1.to_dict()

        # Validate data types of dictionary values after to_dict() conversion
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict["id"], str)
        self.assertIsInstance(obj_dict["__class__"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_save_method(self):
        """ Test the save() method of the BaseModel class.
        Asserts that The 'updated_at' attribute before calling save() is
        not the same after calling save().
        """
        before_save = self.obj_1.updated_at
        after_save = self.obj_1.save()
        # Validate that 'updated_at' attribute is updated after calling save()
        self.assertNotEqual(before_save, after_save)


if __name__ == '__main__':
    unittest.main()