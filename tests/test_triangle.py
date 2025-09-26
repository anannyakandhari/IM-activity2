"""Unit tests for the Triangle class."""

__author__ = "Anannya"
__version__ = "1.0.0"

import unittest
import math
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):
    """Beginner-friendly unit tests for the Triangle class."""

    def setUp(self):
        """Create triangle objects for testing."""
        self.t1 = Triangle("red", 3, 4, 5)    # Right triangle
        self.t2 = Triangle("blue", 6, 6, 6)   # Equilateral
        self.t3 = Triangle("green", 5, 5, 8)  # Isosceles

    # ---------- __str__ method ----------
    def test_str_t1(self):
        """Test __str__ method for right triangle."""
        expected = "The shape color is red.\nThis triangle has three sides with the lengths of 3, 4 and 5 centimeters."
        self.assertEqual(str(self.t1), expected)

    def test_str_t2(self):
        """Test __str__ method for equilateral triangle."""
        expected = "The shape color is blue.\nThis triangle has three sides with the lengths of 6, 6 and 6 centimeters."
        self.assertEqual(str(self.t2), expected)

    # ---------- Area calculation ----------
    def test_area_t1(self):
        """Test area calculation for right triangle."""
        self.assertAlmostEqual(self.t1.calculate_area(), 6.0)

    def test_area_t2(self):
        """Test area calculation for equilateral triangle."""
        sp = (6 + 6 + 6) / 2
        expected_area = math.sqrt(sp * (sp - 6) * (sp - 6) * (sp - 6))
        self.assertAlmostEqual(self.t2.calculate_area(), expected_area)

    def test_area_t3(self):
        """Test area calculation for isosceles triangle."""
        sp = (5 + 5 + 8) / 2
        expected_area = math.sqrt(sp * (sp - 5) * (sp - 5) * (sp - 8))
        self.assertAlmostEqual(self.t3.calculate_area(), expected_area)

    # ---------- Perimeter calculation ----------
    def test_perimeter_all(self):
        """Test perimeter calculation for all triangles."""
        self.assertEqual(self.t1.calculate_perimeter(), 12)
        self.assertEqual(self.t2.calculate_perimeter(), 18)
        self.assertEqual(self.t3.calculate_perimeter(), 18)

    # ---------- Invalid side types ----------
    def test_invalid_sides(self):
        """Test that non-numeric sides raise ValueError."""
        with self.assertRaises(ValueError):
            Triangle("yellow", "a", 4, 5)
        with self.assertRaises(ValueError):
            Triangle("yellow", 3, "b", 5)
        with self.assertRaises(ValueError):
            Triangle("yellow", 3, 4, "c")

    # ---------- Triangle Inequality ----------
    def test_triangle_inequality(self):
        """Test that violating the triangle inequality raises ValueError."""
        with self.assertRaises(ValueError):
            Triangle("orange", 1, 2, 10)
        with self.assertRaises(ValueError):
            Triangle("orange", 1, 10, 2)
        with self.assertRaises(ValueError):
            Triangle("orange", 10, 1, 2)

if __name__ == "__main__":
    unittest.main()
