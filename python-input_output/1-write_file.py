#!/usr/bin/python3
"""
File: 1-write_file.py
Writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file.

    Args:
        filename (str): my_first_file. Defaults to an empty string.
        text (str): Text to write. Defaults to an empty string.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
