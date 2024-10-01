#!/usr/bin/python3
"""
This module provides a function to convert a
Python object to its JSON string representation.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object (my_obj).

    Args:
        my_obj: The object to be converted to JSON string.

    Return:
        str: JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
