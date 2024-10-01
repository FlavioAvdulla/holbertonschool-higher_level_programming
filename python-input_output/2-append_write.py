#!/usr/bin/python3
"""
This module provides a function to append text to a file.

Functions:
    append_write(filename="", text="") -> int:
        Appends the given text to the specified file and
        returns the number of characters written.
"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file.

    Args:
        file_append: The name of the file to append to.
        Defaults to an empty string.
        file_append: The text to append to the file.
        Defaults to an empty string.
    Returns:
        int: The number of the characters written to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
