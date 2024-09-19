#!/usr/bin/python3
"""
Rectangle Module

This module provides a Rectangle class to represent a rectangle with width and height attributes.

Classes:
    Rectangle

Exceptions:
    TypeError: Raised when the width or height is not an integer.
    ValueError: Raised when the width or height is less than 0.
"""

class Rectangle:
    """
    A class used to represent a Rectangle

    Attributes
    ----------
    width : int
        The width of the rectangle (default is 0)
    height : int
        The height of the rectangle (default is 0)

    Methods
    -------
    width():
        Gets the width of the rectangle.
    width(value):
        Sets the width of the rectangle. Raises TypeError if value is not an integer.
        Raises ValueError if value is less than 0.
    height():
        Gets the height of the rectangle.
    height(value):
        Sets the height of the rectangle. Raises TypeError if value is not an integer.
        Raises ValueError if value is less than 0.
    """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object.

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters
        ----------
        value : int
            The width of the rectangle

        Raises
        ------
        TypeError
            If value is not an integer
        ValueError
            If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters
        ----------
        value : int
            The height of the rectangle

        Raises
        ------
        TypeError
            If value is not an integer
        ValueError
            If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
