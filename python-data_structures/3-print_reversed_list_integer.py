#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers in a list in reverse order.

    Args:
        my_list (list): A list of integers.

    Returns:
        None

    Raises:
        ValueError: If the list contains non-integer values.

    Example:
        >>> print_reversed_list_integer([1, 2, 3, 4])
        4
        3
        2
        1
        >>> print_reversed_list_integer([1, 'a', 3])
        ValueError: List contains non-integer value
    """
    if my_list is None:
        return
    for i in range(len(my_list) - 1, -1, -1):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]))
        else:
            raise ValueError("List contains non-integer value")
