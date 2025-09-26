"""Unit tests for the Triangle class."""

__author__ = "Anannya"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):
    """Test cases for the Triangle class."""

    def setUp(self):
        """Common setup for tests."""
        self.triangle = Triangle("red", 3, 4, 5)

    def test_str_method(self):
        """Test the string output of the triangle."""
        expected = (
            "The shape color is red.\n"
            "This triangle has three sides with the lengths of 3, 4 and 5 centimeters."
        )
        self.assertEqual(str(self.triangle), expected)

    def test_area_calculation(self):
        """Test area calculation using Heron's formula."""
        self.assertAlmostEqual(self.triangle.calculate_area(), 6.0)

    def test_perimeter_calculation(self):
        """Test perimeter calculation."""
        self.assertEqual(self.triangle.calculate_perimeter(), 12)

    def test_invalid_side_type(self):
        """Test that non-numeric sides raise ValueError."""
        with self.assertRaises(ValueError) as context:
            Triangle("blue", "a", 4, 5)
        self.assertEqual(str(context.exception), "Side 1 must be numeric.")

    def test_triangle_inequality(self):
        """Test that sides violating triangle inequality raise ValueError."""
        with self.assertRaises(ValueError) as context:
            Triangle("green", 1, 2, 10)
        self.assertEqual(str(context.exception), 
                         "The sides do not satisfy the Triangle Inequality Theorem.")

if __name__ == "__main__":
    unittest.main()
