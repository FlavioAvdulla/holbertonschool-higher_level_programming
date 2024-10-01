#!/usr/bin/python3
"""
This module provides a function to load data from a JSON file.

Functions:
    Loads_from_json_file(filename):
    Reads a JSON file a returns the corresponding
python object.
"""


import json


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
