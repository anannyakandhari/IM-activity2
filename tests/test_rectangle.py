"""Unit tests for the Rectangle class."""

__author__ = "Anannya"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def setUp(self):
        """Setup a valid rectangle before each test."""
        self.rect = Rectangle("blue", 5, 3)

    def test_str_method(self):
        """Test __str__ output."""
        expected = (
            "The shape color is blue.\n"
            "This rectangle has four sides with the lengths of 5, 3, 5 and 3 centimeters."
        )
        self.assertEqual(str(self.rect), expected)

    def test_area(self):
        """Test area calculation."""
        self.assertEqual(self.rect.calculate_area(), 15)

    def test_perimeter(self):
        """Test perimeter calculation."""
        self.assertEqual(self.rect.calculate_perimeter(), 16)

    def test_invalid_length(self):
        """Test that non-numeric length raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle("red", "five", 3)
        self.assertEqual(str(e.exception), "Length must be numeric.")

    def test_invalid_width(self):
        """Test that non-numeric width raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle("red", 5, "three")
        self.assertEqual(str(e.exception), "Width must be numeric.")

if __name__ == "__main__":
    unittest.main()
