#!/usr/bin/python3
"""
This module provides a function to delete a key from a dictionary if it exists.

Functions:
    simple_delete(a_dictionary, key=""): Removes the key from `a_dictionary` if it exists.

Example:
    The function `simple_delete` takes a dictionary `a_dictionary` and a key. If the key exists in the dictionary, it deletes the key-value pair. It returns the modified dictionary.

Usage:
    Call the `simple_delete` function with a dictionary and a key.

    Example:
        a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
        updated_dict = simple_delete(a_dictionary, 'track')
        print(updated_dict)  # Output: {'language': 'C', 'Number': 89, 'ids': [1, 2, 3]}
"""

def simple_delete(a_dictionary, key=""):
    """
    Removes the key from `a_dictionary` if it exists.

    Parameters:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to remove from the dictionary.

    Returns:
        dict: The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
