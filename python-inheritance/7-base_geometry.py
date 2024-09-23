#!/usr/bin/python3
"""
Module: base_geometry

This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class:

    A base class for geometric operations.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
    """
    Validates that value is a positive integer.

    Args:
        name (str): The name of the parameter.
        value (int): The value to validate.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is not greater than 0.
    """
        if value isinstance(self, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
