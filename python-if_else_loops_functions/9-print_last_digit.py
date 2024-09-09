#!/usr/bin/python3
"""
This script defines a function to print and return the last digit of a given number.

Modules:
    None

Functions:
    print_last_digit(number): Prints and returns the last digit of the input number.

Usage:
    Call the print_last_digit(number) function with an integer to print and get its last digit.

Example:
    >>> print_last_digit(123)
    3
    >>> print_last_digit(-456)
    6
"""

def print_last_digit(number):
    """
    Print and return the last digit of the input number.

    Args:
        number (int): The input number.

    Returns:
        int: The last digit of the input number.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
