#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all occurrences of the characters 'c' and 'C' from a string.

    Args:
        my_string (str): The original string.

    Returns:
        str: A new string with all 'c' and 'C' characters removed.

    Example:
        >>> no_c("Chocolate Cake")
        'hoolate ake'
        >>> no_c("Civic Center")
        'ivi enter'
    """
    new_string = ''.join(char for char in my_string if char not in 'cC')
    return new_string
