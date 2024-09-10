#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Creates a copy of a list with an element replaced at a specific index.

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element.
        element: The new element to place at the specified index.

    Returns:
        list: A new list with the element replaced, or a copy of the original list if the index is out of range.

    Example:
        >>> new_in_list([1, 2, 3, 4], 2, 9)
        [1, 2, 9, 4]
        >>> new_in_list([1, 2, 3, 4], -1, 9)
        [1, 2, 3, 4]
        >>> new_in_list([1, 2, 3, 4], 4, 9)
        [1, 2, 3, 4]
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
