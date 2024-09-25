#!/usr/bin/python3
"""
Module for shapes with area and perimeter calculations.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle shape with radius.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """
    Rectangle shape with width and height.
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
    print(f"Perimeter: {shape.perimeter()}")
    print(f"Area: {shape.area()}")
