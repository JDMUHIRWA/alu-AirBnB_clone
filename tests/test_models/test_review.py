import unittest
from datetime import datetime
from models.review import Review


class TestReviewAttributes(unittest.TestCase):
    """
     Defines a Test case class for the Review attributes in the
     models.review module.
    """

    def test_place_id(self):
        """
        Test if the place_id attribute of Review is a string
        and has the default value of an empty string.
        """
        self.assertIsInstance(Review.place_id, str)
        self.assertEqual(Review.place_id, "")

    def test_user_id(self):
        """ validate user_id attribute of Review is a string and
        has the default value of an empty string.
        """
        self.assertIsInstance(Review.user_id, str)

    def test_default_id(self):
        """ Test the user_id has the
        default value of an empty string."""
        self.assertEqual(Review.user_id, "")

    def test_text(self):
        """ Test that text'attribute of Review is a string and has
        the default value of an empty string.
        """
        self.assertIsInstance(Review.text, str)
        self.assertEqual(Review.text, "")

    def test_user_id_assignment(self):
        """ Test if assigning a value to user_id attribute of
        Review updates the attribute correctly.
        """
        review = Review()
        review.user_id = "Manny.Daedlus"
        self.assertEqual(review.user_id, "Manny.Daedlus")

    def test_text_assignment(self):
        """ Test if assigning a value to text attribute of Review
        updates the attribute correctly.
        """
        review = Review()
        rev_text = "Nice web App from Manny And Elgibbor. lol!"
        review.text = rev_text
        self.assertEqual(review.text, rev_text)


if __name__ == '__main__':
    unittest.main()