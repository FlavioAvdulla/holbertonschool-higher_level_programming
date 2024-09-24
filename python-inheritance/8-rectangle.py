#!/usr/bin/python3
"""
Rectangle Module

This module provides a Rectangle class that inherits from BaseGeometry.
The Rectangle class includes methods for initializing the rectangle with
width and height, validating these dimensions, and providing a string
representation of the rectangle.

Classes:
    Rectangle

Usage Example:
    >>> from rectangle import Rectangle
    >>> r = Rectangle(3, 4)
    >>> print(r)
    [Rectangle] 3/4
"""


from base_geometry import BaseGeometry  # Ensure this import matches your actual module structure

class Rectangle(BaseGeometry):
    """
    A Rectangle class inheriting from BaseGeometry.

    Methods:
        __init__(self, width, height): Initializes with width and height.
        __str__(self): Returns a string representation.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.

        Parameters:
        width (int): The width of the rectangle, must be a positive integer.
        height (int): The height of the rectangle, must be a positive integer.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
        str: A string in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
