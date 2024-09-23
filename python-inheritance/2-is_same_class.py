#!/usr/bin/python3
"""
Check if an object is exactly an instance of a specified class.

Functions:
    is_same_class(obj, a_class): Returns True if obj is an instance of a_class, else False.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
