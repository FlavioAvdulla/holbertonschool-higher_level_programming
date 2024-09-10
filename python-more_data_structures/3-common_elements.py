#!/usr/bin/python3
"""
This module provides a function to find common elements between two sets.

Functions:
    common_elements(set_1, set_2): Returns a set containing the common elements of `set_1` and `set_2`.

Example:
    The function `common_elements` takes two sets `set_1` and `set_2` and returns a new set containing the elements that are present in both sets.

Usage:
    Call the `common_elements` function with two sets.

    Example:
        set_1 = {1, 2, 3, 4}
        set_2 = {3, 4, 5, 6}
        result = common_elements(set_1, set_2)
        print(result)  # Output: {3, 4}
"""

def common_elements(set_1, set_2):
    """
    Returns a set containing the common elements of `set_1` and `set_2`.

    Parameters:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing the common elements of `set_1` and `set_2`.
    """
    set_3 = set_1.intersection(set_2)
    return set_3
