#!/usr/bin/python3
"""
File: read_file_module.py
Author: Your Name
Description: This module provides a function to read and print the contents of a text file.
"""
def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open('filename', 'r', encoding='utf-8') as file:
        print(file.read())