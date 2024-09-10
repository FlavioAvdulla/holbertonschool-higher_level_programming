#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific index.

    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index at which to replace the element.
        element: The new element to place at the specified index.

    Returns:
        list: The modified list with the element replaced, or the original list if the index is out of range.

    Example:
        >>> replace_in_list([1, 2, 3, 4], 2, 9)
        [1, 2, 9, 4]
        >>> replace_in_list([1, 2, 3, 4], -1, 9)
        [1, 2, 3, 4]
        >>> replace_in_list([1, 2, 3, 4], 4, 9)
        [1, 2, 3, 4]
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
