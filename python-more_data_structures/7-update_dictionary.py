#!/usr/bin/python3
"""
This module provides a function to update a dictionary with a new key-value pair or modify an existing key with a new value.

Functions:
    update_dictionary(a_dictionary, key, value): Updates `a_dictionary` with the key-value pair (`key`, `value`).

Example:
    The function `update_dictionary` takes a dictionary `a_dictionary`, a key, and a value. It updates the dictionary with the new key-value pair or modifies the existing key with the new value.

Usage:
    Call the `update_dictionary` function with a dictionary, a key, and a value.

    Example:
        a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
        updated_dict = update_dictionary(a_dictionary, 'language', "Python")
        print(updated_dict)  # Output: {'language': 'Python', 'number': 89, 'track': 'Low level'}
"""

def update_dictionary(a_dictionary, key, value):
    """
    Updates `a_dictionary` with the key-value pair (`key`, `value`).

    Parameters:
        a_dictionary (dict): The dictionary to update.
        key: The key to add or update in the dictionary.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
