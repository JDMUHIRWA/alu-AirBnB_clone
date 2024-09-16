#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlaceAttributes(unittest.TestCase):
    """
    Test case class for the Place attributes in the models.Place module.
    """

    def test_city_id(self):
        """
        Test if the city_id attribute of Place is a string and has the default
        value of an empty string.
        """
        self.assertIsInstance(Place.city_id, str)
        self.assertEqual(Place.city_id, "")

    def test_user_id(self):
        """ Test if the user_id attribute of Place is a string and has
        the default value of an empty string.
        """
        self.assertIsInstance(Place.user_id, str)
        self.assertEqual(Place.user_id, "")

    def test_name(self):
        """ Test if the "ame attribute of Place is a string and has the default
        value of an empty string.
        """
        self.assertIsInstance(Place.name, str)
        self.assertEqual(Place.name, "")

    def test_description(self):
        """ Test if the description attribute of Place is a string and
        has the default value of an empty string.
        """
        self.assertIsInstance(Place.description, str)
        self.assertEqual(Place.description, "")

    def test_number_rooms(self):
        """ Test if the number_rooms attribute of Place is an integer and
        has the default value of 0.
        """
        self.assertIsInstance(Place.number_rooms, int)
        self.assertEqual(Place.number_rooms, 0)

    def test_number_bathrooms(self):
        """ Test if the number_bathrooms attribute of Place is an integer
        and has the default value of 0.
        """
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertEqual(Place.number_bathrooms, 0)

    def test_max_guest(self):
        """ Test if the max_guest attribute of Place is an integer and has the
        default value of 0.
        """
        self.assertIsInstance(Place.max_guest, int)
        self.assertEqual(Place.max_guest, 0)

    def test_price_by_night(self):
        """ Test if the 'price_by_night' attribute of Place is an integer and
        has the default value of 0.
        """
        self.assertIsInstance(Place.price_by_night, int)
        self.assertEqual(Place.price_by_night, 0)

    def test_latitude(self):
        """ Test if the latitude attribute of Place is a float and has the
        default value of 0.0.
        """
        self.assertIsInstance(Place.latitude, float)
        self.assertEqual(Place.latitude, 0.0)

    def test_longitude(self):
        """ Test if the 'longitude' attribute of Place is a float and has the
        default value of 0.0.
        """
        self.assertIsInstance(Place.longitude, float)
        self.assertEqual(Place.longitude, 0.0)


if __name__ == '__main__':
    unittest.main()