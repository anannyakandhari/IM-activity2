"""This module defines the Shape abstract class."""

# ABC = Abstract Base Class
# It allows us to create abstract methods that must
# be implemented in child classes
from abc import ABC, abstractmethod

__author__ = "Anannya"
__version__ = "1.0.0"


class Shape(ABC):
    """
    An abstract base class for different shapes.
    Provides a template for color, area, and perimeter.
    """

    def __init__(self, color):
        """
        Initialize a Shape object.

        Args:
            color (str): The color of the shape.

        Raises:
            ValueError: If color is blank or only spaces.
        """
        color = color.strip()
        if not color:
            raise ValueError("Color cannot be blank.")
        self._color = color  # Protected attribute

    def __str__(self):
        """
        Return a string description of the shape color.

        Returns:
            str: A message about the shape's color.
        """
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self):
        """
        Abstract method for calculating the area of the shape.
        Must be implemented in subclasses.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self):
        """
        Abstract method for calculating the perimeter of the shape.
        Must be implemented in subclasses.
        """
        pass
