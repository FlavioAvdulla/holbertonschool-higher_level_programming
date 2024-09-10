#!/usr/bin/python3
"""
This module provides a function to find elements that are unique to each of two sets.

Functions:
    only_diff_elements(set_1, set_2): Returns a set containing the elements that are unique to each set.

Example:
    The function `only_diff_elements` takes two sets `set_1` and `set_2` and returns a new set containing the elements that are in either `set_1` or `set_2` but not in both.

Usage:
    Call the `only_diff_elements` function with two sets.

    Example:
        set_1 = {"Python", "C", "Javascript"}
        set_2 = {"Bash", "C", "Ruby", "Perl"}
        result = only_diff_elements(set_1, set_2)
        print(result)  # Output: {'Python', 'Ruby', 'Bash', 'Javascript', 'Perl'}
"""

def only_diff_elements(set_1, set_2):
    """
    Returns a set containing the elements that are unique to each set.

    Parameters:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing the elements that are unique to each set.
    """
    return set_1.symmetric_difference(set_2)
