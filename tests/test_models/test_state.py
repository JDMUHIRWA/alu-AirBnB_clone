#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """
    Test case class for the State class, a subclass of BaseModel.
    """
    def setUp(self):
        """ Test if State object is successfully created."""
        self.state = State()

    def test_instance_creation(self):
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """ Test if State class inherits from BaseModel. """
        self.assertTrue(issubclass(State, BaseModel))

    def test_name_attribute(self):
        """ Test if name attribute is present in the State class."""
        self.assertTrue(hasattr(State, 'name'))

    def test_name_attribute_type(self):
        """ Test if name attribute in State is a string."""
        self.assertIsInstance(State.name, str)

    def test_name_assignment(self):
        """ Test if assigning a value to name attribute of State
        updates the attribute correctly."""
        state = State()
        state.name = "Dubai, UAE"
        self.assertEqual(state.name, "Dubai, UAE")

    def test_inherited_attributes(self):
        """
        Confirm that all default superclass attributes are inherited
        """
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)


if __name__ == '__main__':
    unittest.main()