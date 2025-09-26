"""Unit tests for the Rectangle class."""

__author__ = "Anannya"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Beginner-friendly tests for Rectangle class."""

    def setUp(self):
        """Create some rectangle objects for testing."""
        self.r1 = Rectangle("blue", 5, 3)
        self.r2 = Rectangle("red", 10, 2)

    # ---------- __str__ method ----------
    def test_str(self):
        expected1 = "The shape color is blue.\nThis rectangle has four sides with the lengths of 5, 3, 5 and 3 centimeters."
        expected2 = "The shape color is red.\nThis rectangle has four sides with the lengths of 10, 2, 10 and 2 centimeters."
        self.assertEqual(str(self.r1), expected1)
        self.assertEqual(str(self.r2), expected2)

    # ---------- Area calculation ----------
    def test_area(self):
        self.assertEqual(self.r1.calculate_area(), 15)
        self.assertEqual(self.r2.calculate_area(), 20)

    # ---------- Perimeter calculation ----------
    def test_perimeter(self):
        self.assertEqual(self.r1.calculate_perimeter(), 16)
        self.assertEqual(self.r2.calculate_perimeter(), 24)

    # ---------- Invalid length ----------
    def test_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("green", "wrong", 4)
        self.assertEqual(str(context.exception), "Length must be numeric.")

    # ---------- Invalid width ----------
    def test_invalid_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("green", 5, "wrong")
        self.assertEqual(str(context.exception), "Width must be numeric.")

    # ---------- Zero dimensions ----------
    def test_zero_length_width(self):
        r = Rectangle("black", 0, 0)
        self.assertEqual(r.calculate_area(), 0)
        self.assertEqual(r.calculate_perimeter(), 0)

    # ---------- Large numbers ----------
    def test_large_numbers(self):
        r = Rectangle("yellow", 1000, 2000)
        self.assertEqual(r.calculate_area(), 2_000_000)
        self.assertEqual(r.calculate_perimeter(), 6000)

if __name__ == "__main__":
    unittest.main()
