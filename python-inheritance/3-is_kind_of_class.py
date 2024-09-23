#!/usr/bin/python3
"""
Check if an object is an instance of a specified class or its subclass.

Functions:
    is_kind_of_class(obj, a_class): Returns True if obj is an instance of a_class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or its subclass.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a_class or its subclass, else False.
    """
    return isinstance(obj, a_class)
