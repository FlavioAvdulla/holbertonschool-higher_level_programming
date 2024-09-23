#!/usr/bin/python3
"""
Module to list attributes and methods of an object.

Functions:
    lookup(obj): Returns a list of attributes and methods.
"""

def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of attribute and method names.
    """
    return dir(obj)
