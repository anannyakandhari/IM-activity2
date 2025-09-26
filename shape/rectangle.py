"""This module defines the Rectangle class."""

__author__ = ""
__version__ = ""

# rectangle.py

from shape.shape import Shape

class Rectangle(Shape):
    """
    A Rectangle class that inherits from Shape.
    Represents a rectangle with a given length and width.
    """

    def __init__(self, color, length, width):
        """
        Initialize a Rectangle object.

        Args:
            color (str): The color of the rectangle.
            length (int): The length of the rectangle (must be numeric).
            width (int): The width of the rectangle (must be numeric).

        Raises:
            ValueError: If length or width is not an integer.
        """
        super().__init__(color)

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        self._length = length

        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")
        self._width = width

    def __str__(self):
        """
        Return a string description of the rectangle.

        Returns:
            str: A description including the color and side lengths.
        """
        return (
            f"{super().__str__()}\n"
            f"This rectangle has four sides with the lengths of "
            f"{self._length}, {self._width}, {self._length}, and {self._width} centimeters."
        )

    def calculate_area(self):
        """
        Calculate the area of the rectangle.

        Formula:
            area = length * width

        Returns:
            int: The area of the rectangle.
        """
        return self._length * self._width

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Formula:
            perimeter = 2 * (length + width)

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self._length + self._width)
