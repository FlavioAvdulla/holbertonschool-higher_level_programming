#!/usr/bin/env python3
"""
This module defines an abstract base class for shapes and demonstrates
duck typing by implementing concrete classes for Circle and Rectangle.
It also includes a function to print the area and perimeter of any shape.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class for shapes.
    Defines the blueprint for shape objects with area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    """
    Circle class inheriting from Shape.
    Implements the area and perimeter methods for a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        
        :param radius: Radius of the circle
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape.
    Implements the area and perimeter methods for a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with a given width and height.
        
        :param width: Width of the rectangle
        :param height: Height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    
    :param shape: An object of type Shape (duck typing)
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
