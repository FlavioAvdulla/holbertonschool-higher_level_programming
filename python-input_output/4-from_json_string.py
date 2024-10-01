#!/usr/bin/python3
"""
This module provides a function that
returns an object (Python data structure)
represented by a JSON string.
"""


import json

def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        my_str: A string containing JSON data.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
