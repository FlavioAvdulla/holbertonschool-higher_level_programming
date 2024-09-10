#!/usr/bin/python3
"""
This module provides a function to create a new dictionary with all values multiplied by 2.

Functions:
    multiply_by_2(a_dictionary): Returns a new dictionary with all values multiplied by 2.

Example:
    The function `multiply_by_2` takes a dictionary `a_dictionary` and returns a new dictionary where each value is multiplied by 2.

Usage:
    Call the `multiply_by_2` function with a dictionary.

    Example:
        a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
        new_dict = multiply_by_2(a_dictionary)
        print(new_dict)  # Output: {'John': 24, 'Alex': 16, 'Bob': 28, 'Mike': 28, 'Molly': 32}
"""

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Parameters:
        a_dictionary (dict): The dictionary to process.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
