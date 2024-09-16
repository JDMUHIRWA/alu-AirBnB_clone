import unittest
from models.city import City
from models.base_model import BaseModel


class TestCityClass(unittest.TestCase):
    """
    Test case class for the City class in the models.city module.
    """
    def test_instance_creation(self):
        """ Test if City object is successfully created."""
        city = City()
        self.assertIsInstance(city, City)

    def test_inheritance(self):
        """ Test if City class inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_state_id_attribute(self):
        """ Test if state_id attribute is present in the City class."""
        self.assertTrue(hasattr(City, 'state_id'))

    def test_state_id_attribute_type(self):
        """ Test if 'state_id' attribute in City is a string."""
        self.assertIsInstance(City.state_id, str)

    def test_name_attribute(self):
        """ Test if 'name' attribute is present in the City class."""
        self.assertTrue(hasattr(City, 'name'))

    def test_name_attribute_type(self):
        """ Test if 'name' attribute in City is a string."""
        self.assertIsInstance(City.name, str)


if __name__ == '__main__':
    unittest.main()