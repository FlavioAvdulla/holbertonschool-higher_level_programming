#!/usr/bin/python3
"""
File: 1- 1-write_file.py
Author: Flavio Avdulla
This module provides a function to write a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename: The name of the file to write to. Defaults to an empty string.
        text: The text to write to the file.
        Defaults to an empty string.

    Returns:
        int: The number of the characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
