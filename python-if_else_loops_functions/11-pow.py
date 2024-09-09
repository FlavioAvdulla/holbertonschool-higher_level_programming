#!/usr/bin/python3
"""
This script defines a function to calculate the power of one number raised to another.

Modules:
    None

Functions:
    pow(a, b): Returns the result of a raised to the power of b.

Usage:
    Call the pow(a, b) function with two numbers to get the result of a raised to the power of b.

Example:
    >>> pow(2, 3)
    8
    >>> pow(5, 2)
    25
"""

def pow(a, b):
    """
    Calculate the power of a raised to b.

    Args:
        a (int or float): The base number.
        b (int or float): The exponent.

    Returns:
        int or float: The result of a raised to the power of b.
    """
    return a ** b
