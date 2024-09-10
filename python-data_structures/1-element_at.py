#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list at a specific index.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index if it exists, otherwise None.

    Example:
        >>> element_at([1, 2, 3, 4], 2)
        3
        >>> element_at([1, 2, 3, 4], -1)
        None
        >>> element_at([1, 2, 3, 4], 4)
        None
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
