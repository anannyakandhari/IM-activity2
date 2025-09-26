from abc import ABC, abstractmethod

__author__ = "Anannya"
__version__ = "1.0.0"

class Shape(ABC):
    """Abstract base class for all shapes."""

    def __init__(self, color):
        if not color or not color.strip():
            raise ValueError("Color cannot be blank.")
        self._color = color.strip()

    def __str__(self):
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass
