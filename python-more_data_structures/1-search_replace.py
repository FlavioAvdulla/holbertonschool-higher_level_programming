#!/usr/bin/python3
"""
This module provides a function to replace all occurrences of a specified element in a list with a new element.

Functions:
    search_replace(my_list, search, replace): Replaces all occurrences of `search` in `my_list` with `replace`.

Example:
    The function `search_replace` takes a list `my_list` and replaces all occurrences of the element `search` with the element `replace`. It returns a new list with the replacements made.

Usage:
    Call the `search_replace` function with a list and the elements to search and replace.

    Example:
        my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
        new_list = search_replace(my_list, 2, 89)
        print(new_list)  # Output: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
"""

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of `search` in `my_list` with `replace`.

    Parameters:
        my_list (list): The list to process.
        search: The element to search for in the list.
        replace: The element to replace `search` with.

    Returns:
        list: A new list with the replacements made.
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
