#!/usr/bin/python3
"""
This module defines a Square class that inherits from BaseGeometry.

Classes:
    Square: Represents a square with methods to initialize and calculate its area.
"""


BaseGeometry = __import__('9-rectangle').BaseGeometry

class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from Rectangle

    ...

    Attributes
    ----------
    __size : int
        The size of the square's sides, must be a positive integer

    Methods
    -------
    __init__(self, size):
        Initializes the square with the given size after validation

    area(self):
        Calculates and returns the area of the square
    """

    def __init__(self, size):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
        size : int
            The size of the square's sides, must be a positive integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square
        """
        return self.__size ** 2
