"""This module defines the Rectangle class."""

from shape import Shape

__author__ = "Anannya"
__version__ = "1.0.0"

class Rectangle(Shape):
    """Represents a rectangle shape."""

    def __init__(self, color, length, width):
        """Initialize a Rectangle

        Args:
            color (str): Color of the rectangle.
            length (int): Length of rectangle sides.
            width (int): Width of rectangle sides.

        Raises:
            ValueError: If length or width is not numeric.
        """
        super().__init__(color)

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")

        self._length = length
        self._width = width

    def __str__(self):
        """Return a string description of the rectangle."""
        return (
            f"{super().__str__()}\n"
            f"This rectangle has four sides with the lengths of"
            f"{self._length}, {self._width}, {self._length} and {self._width} centimeters."
        )

    def calculate_area(self):
        """Return the area of the rectangle."""
        return self._length * self._width

    def calculate_perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self._length + self._width)
