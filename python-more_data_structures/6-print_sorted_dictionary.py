#!/usr/bin/python3
"""
This module provides a function to print the keys and values of a dictionary in sorted order by keys.

Functions:
    print_sorted_dictionary(a_dictionary): Prints the keys and values of `a_dictionary` sorted by keys.

Example:
    The function `print_sorted_dictionary` takes a dictionary `a_dictionary` and prints its keys and values in sorted order by keys.

Usage:
    Call the `print_sorted_dictionary` function with a dictionary.

    Example:
        a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
        print_sorted_dictionary(a_dictionary)
        # Output:
        # Number: 89
        # ids: [1, 2, 3]
        # language: C
        # track: Low level
"""

def print_sorted_dictionary(a_dictionary):
    """
    Prints the keys and values of `a_dictionary` sorted by keys.

    Parameters:
        a_dictionary (dict): The dictionary to process.

    Returns:
        None
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
