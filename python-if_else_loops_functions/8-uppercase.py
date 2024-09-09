#!/usr/bin/python3
"""
This script defines a function to convert all lowercase letters in a string to uppercase.

Modules:
    None

Functions:
    uppercase(str): Converts all lowercase letters in the input string to uppercase and prints the result.

Usage:
    Call the uppercase(str) function with a string to convert its lowercase letters to uppercase.

Example:
    >>> uppercase('hello')
    HELLO
    >>> uppercase('Hello World!')
    HELLO WORLD!
"""

def uppercase(str):
    """
    Convert all lowercase letters in the input string to uppercase.

    Args:
        str (str): The input string to be converted.

    Returns:
        None
    """
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
