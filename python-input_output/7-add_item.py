#!/usr/bin/python3
"""
This module provides a a script that adds all
arguments to a Python list, and then save them to a file:
"""


import sys
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


def load_from_json_file(filename):
    """
    Load data from a JSON file and return it as a Python object.

    Args:
        filename: The name of the file to read from.

    Returns:
        Object: The python object represented by JSON data in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)


filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
