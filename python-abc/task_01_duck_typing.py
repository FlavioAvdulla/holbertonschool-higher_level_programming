#!/usr/bin/python3
"""
This module defines abstract and concrete classes for different shapes.
It includes methods to calculate the area and perimeter of the shapes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    """
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Concrete class for a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Concrete class for a rectangle, inheriting from Shape.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print the perimeter and area of a shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
