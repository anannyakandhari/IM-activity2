"""This module defines the Triangle class."""

from shape import Shape
import math

__author__ = "Anannya"
__version__ = "1.0.0"

class Triangle(Shape):
    """Represents a triangle shape."""

    def __init__(self, color, side_1, side_2, side_3):
        """Initialize a Triangle.

        Args:
            color (str): Color of the triangle.
            side_1 (int): First side.
            side_2 (int): Second side.
            side_3 (int): Third side.

        Raises:
            ValueError: If sides are not numeric or don't satisfy triangle inequality.
        """
        super().__init__(color)

        for i, side in enumerate([side_1, side_2, side_3], start=1):
            if not isinstance(side, int):
                raise ValueError(f"Side {i} must be numeric.")

        if (side_1 + side_2 <= side_3 or
            side_1 + side_3 <= side_2 or
            side_2 + side_3 <= side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")

        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def __str__(self):
        """Return a string description of the triangle."""
        return (
            f"{super().__str__()}\n"
            f"This triangle has three sides with the lengths of "
            f"{self._side_1}, {self._side_2} and {self._side_3} centimeters."
        )

    def calculate_area(self):
        """Return the area of the triangle using Heron's formula."""
        sp = self.calculate_perimeter() / 2
        return math.sqrt(sp * (sp - self._side_1) * (sp - self._side_2) * (sp - self._side_3))

    def calculate_perimeter(self):
        """Return the perimeter of the triangle."""
        return self._side_1 + self._side_2 + self._side_3
