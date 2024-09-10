#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers in a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        None

    Example:
        >>> print_list_integer([1, 2, 3])
        1
        2
        3
    """
    for i in my_list:
        print("{:d}".format(i))
