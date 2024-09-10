#!/usr/bin/python3
"""
This module provides a function to count the number of keys in a dictionary.

Functions:
    number_keys(a_dictionary): Returns the number of keys in `a_dictionary`.

Example:
    The function `number_keys` takes a dictionary `a_dictionary` and returns the number of keys in the dictionary.

Usage:
    Call the `number_keys` function with a dictionary.

    Example:
        a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
        nb_keys = number_keys(a_dictionary)
        print("Number of keys: {:d}".format(nb_keys))  # Output: Number of keys: 3
"""

def number_keys(a_dictionary):
    """
    Returns the number of keys in `a_dictionary`.

    Parameters:
        a_dictionary (dict): The dictionary to process.

    Returns:
        int: The number of keys in the dictionary.
    """
    return len(a_dictionary.keys())
