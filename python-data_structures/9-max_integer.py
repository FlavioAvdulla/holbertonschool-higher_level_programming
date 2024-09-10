#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the maximum integer in a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        int or None: The maximum integer in the list, or None if the list is empty.

    Example:
        >>> max_integer([1, 2, 3, 4])
        4
        >>> max_integer([])
        None
    """
    if not my_list:
        return None
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
