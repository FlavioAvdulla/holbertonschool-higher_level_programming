#!/usr/bin/python3
"""
This module provides a function to save an object to a file in JSON FORMAT.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved.
        filename: The name of the file to save the object to.

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
