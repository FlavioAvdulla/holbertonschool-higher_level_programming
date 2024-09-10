#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes an element from a list at a specific index.

    Args:
        my_list (list): The list from which to delete the element.
        idx (int): The index of the element to delete.

    Returns:
        list: The modified list with the element deleted, or the original list if the index is out of range.

    Example:
        >>> delete_at([1, 2, 3, 4], 2)
        [1, 2, 4]
        >>> delete_at([1, 2, 3, 4], -1)
        [1, 2, 3, 4]
        >>> delete_at([1, 2, 3, 4], 4)
        [1, 2, 3, 4]
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
