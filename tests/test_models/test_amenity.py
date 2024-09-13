
#!/usr/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityClass(unittest.TestCase):
    """
    Test case class for the Amenity class in the models.amenity module.
    """
    def test_inheritance(self):
        """ Test if Amenity class inherits from BaseModel. """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name_attribute(self):
        """ Test if name attribute is present in the Amenity class."""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_to_dict_method(self):
        """ Test if the to_dict() method of Amenity returns the
        expected dictionary.
        """
        amenity = Amenity()
        amenity.name = "Pool"
        amenity_dict = amenity.to_dict()
        expected_dict = {
            'id': amenity.id,
            'created_at': amenity.created_at.isoformat(),
            'updated_at': amenity.updated_at.isoformat(),
            'name': 'Pool',
            '__class__': 'Amenity'
        }
        self.assertEqual(amenity_dict, expected_dict)

    def test_name_attribute_type(self):
        """ Test if name attribute in Amenity is a string."""
        self.assertIsInstance(Amenity.name, str)

    def test_instance_creation(self):
        """ Test if Amenity object is successfully created."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_name_assignment(self):
        """ Test if assigning a value to name attribute of Amenity
        updates the attribute correctly.
        """
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()
