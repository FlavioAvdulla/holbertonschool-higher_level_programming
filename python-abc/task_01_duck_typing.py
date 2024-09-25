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
    
    Methods
    -------
    area() :
        Calculate the area of the shape.
    perimeter() :
        Calculate the perimeter of the shape.
    """

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
    
    Attributes
    ----------
    radius : float
        The radius of the circle.
    
    Methods
    -------
    area() :
        Calculate the area of the circle.
    perimeter() :
        Calculate the perimeter of the circle.
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
    
    Attributes
    ----------
    width : float
        The width of the rectangle.
    height : float
        The height of the rectangle.
    
    Methods
    -------
    area() :
        Calculate the area of the rectangle.
    perimeter() :
        Calculate the perimeter of the rectangle.
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
    
    Parameters
    ----------
    shape : Shape
        An instance of a class that inherits from Shape.
    """
    print(f"Perimeter: {shape.perimeter()}")
    print(f"Area: {shape.area()}")


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
