#!/usr/bin/python3
"""
This script defines a function to check if a given character is a lowercase letter.

Modules:
    None

Functions:
    islower(c): Checks if the character c is a lowercase letter.

Usage:
    Call the islower(c) function with a character to check if it is a lowercase letter.

Example:
    >>> islower('a')
    True
    >>> islower('A')
    False
"""

def islower(c):
    """
    Check if the character c is a lowercase letter.

    Args:
        c (str): A single character to check.

    Returns:
        bool: True if c is a lowercase letter, False otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')
