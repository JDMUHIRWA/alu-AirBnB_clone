#!/usr/bin/env python3
"""
Module for User class
"""
import os
import models
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    def setUp(self):
        self.test_file = "file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_one_save(self):
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_user_attributes(self):
        test_user = User()
        self.assertEqual(hasattr(test_user."email"))
        self.assertEqual(hasattr(test_user."password"))
        self.assertEqual(hasattr(test_user."first_name"))
        self.assertEqual(hasattr(test_user."last_name"))

    def test_user_inherits_from_BaseModel(self):
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        test_user = User()
        test.user.email = "muhirwa@gmail.com"
        test.user.first_name = "Muhirwa"
        test.user.last_name = "JD"
        test.user.password = "password"

        user_str = str(test_user)
        self.assertIn("[User]", user_str)
        self.assertIn("'muhirwa@gmail.com'", user_str)
        self.assertIn("'Muhirwa'", user_str)
        self.assertIn("'JD'", user_str)

    def test_user_to_dict(self):
        test_user = User()
        test_user.email = "muhirwa@gmail.com"
        test_user.first_name = "Muhirwa"
        test_user.last_name = "JD"
        test_user.password = "password"
        test_user.save()

        user_dict = test_user.to_dict()
        self.assertEqual(user_dict["email"], "muhirwa@gmail.com")
        self.assertEqual(user_dict["first_name"], "Muhirwa")
        self.assertEqual(user_dict["last_name"], "JD")

    def test_user_instance_creation(self):
        test_user = User(email="muhirwa@gmail.com",
                         first_name="Muhirwa", last_name="JD", password="password")
        self.assertEqual(test_user.email, "muhirwa@gmail.com")
        self.assertEqual(test_user.first_name, "Muhirwa")
        self.assertEqual(test_user.last_name, "JD")
        self.assertEqual(test_user.password, "password")

    def test_user_id_generation(self):
        test_user1 = User()
        user2 = User()
        self.assertNotEqual(test_user1.id, user2.id)


if __name__ == "__main__":
    unittest.main()
