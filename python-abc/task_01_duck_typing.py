#!/usr/bin/python3
"""
shapes.py

Abstract base class and concrete shapes.
Prints area and perimeter using duck typing.

Classes:
    Shape: Abstract base class.
    Circle: Concrete class.
    Rectangle: Concrete class.

Functions:
    shape_info(shape): Prints area and perimeter.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete class for circles."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class for rectangles."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
