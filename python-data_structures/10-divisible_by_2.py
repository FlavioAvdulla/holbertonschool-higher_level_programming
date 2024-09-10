#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Checks which elements in a list are divisible by 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of boolean values where True indicates the corresponding element in the input list is divisible by 2, and False otherwise.

    Example:
        >>> divisible_by_2([1, 2, 3, 4])
        [False, True, False, True]
        >>> divisible_by_2([10, 15, 20])
        [True, False, True]
    """
    return [num % 2 == 0 for num in my_list]
