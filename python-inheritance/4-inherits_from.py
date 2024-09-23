#!/usr/bin/python3
"""
Check if an object is an instance of a class that inherited from a specified class.

Functions:
    inherits_from(obj, a_class): Returns True if obj is an instance of a subclass of a_class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a subclass of a_class, else False.
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
