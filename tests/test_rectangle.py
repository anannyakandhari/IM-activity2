"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Anannya"
__version__ = "1.0" 

# test_rectangle.py

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def setUp(self):
        """Common setup for tests."""
        self.rectangle = Rectangle("blue", 5, 3)

    def test_str_method(self):
        """Test the string output of the rectangle."""
        expected = (
            "The shape color is blue.\n"
            "This rectangle has four sides with the lengths of 5, 3, 5, and 3 centimeters."
        )
        self.assertEqual(str(self.rectangle), expected)

    def test_area_calculation(self):
        """Test area calculation (length * width)."""
        self.assertEqual(self.rectangle.calculate_area(), 15)

    def test_perimeter_calculation(self):
        """Test perimeter calculation (2 * (length + width))."""
        self.assertEqual(self.rectangle.calculate_perimeter(), 16)

    def test_invalid_length(self):
        """Test that non-numeric length raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Rectangle("red", "not_number", 4)
        self.assertEqual(str(context.exception), "Length must be numeric.")

    def test_invalid_width(self):
        """Test that non-numeric width raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Rectangle("red", 5, "wrong")
        self.assertEqual(str(context.exception), "Width must be numeric.")

if __name__ == "__main__":
    unittest.main()
