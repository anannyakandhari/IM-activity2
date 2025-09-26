"""This module defines the Triangle class."""

__author__ = "anannya"
__version__ = "1.0"

# triangle.py

from shape.shape import Shape

class Triangle(Shape):
    """
    A Triangle class that inherits from Shape.
    Represents a triangle with three side lengths.
    """

    def __init__(self, color, side1, side2, side3):
        """
        Initialize a Triangle object.

        Args:
            color (str): The color of the triangle.
            side1 (int): Length of the first side.
            side2 (int): Length of the second side.
            side3 (int): Length of the third side.

        Raises:
            ValueError: If any side is not numeric.
        """
        super().__init__(color)

        if not all(isinstance(side, int) for side in (side1, side2, side3)):
            raise ValueError("All sides must be numeric.")

        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def __str__(self):
        """
        Return a string description of the triangle.

        Returns:
            str: A description with color and side lengths.
        """
        return (
            f"{super().__str__()}\n"
            f"This triangle has three sides with lengths of "
            f"{self._side1}, {self._side2}, and {self._side3} centimeters."
        )

    def calculate_area(self):
        """
        Calculate the area using Heron's formula.

        Formula:
            s = (a + b + c) / 2
            area = sqrt(s * (s - a) * (s - b) * (s - c))

        Returns:
            float: The area of the triangle.
        """
        import math
        s = (self._side1 + self._side2 + self._side3) / 2
        return math.sqrt(
            s * (s - self._side1) * (s - self._side2) * (s - self._side3)
        )

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the triangle.

        Formula:
            perimeter = side1 + side2 + side3

        Returns:
            int: The perimeter of the triangle.
        """
        return self._side1 + self._side2 + self._side3
