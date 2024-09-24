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
class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.

    ...

    Methods
    -------
    __init__(self, width, height)
        Initializes the Rectangle with width and height, validating them as positive integers.

    __Str__(self)
        Returns a string representation of the Rectangle.
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
        self.__width = width
        self.__height = height

    def __Str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
        str: A string in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
