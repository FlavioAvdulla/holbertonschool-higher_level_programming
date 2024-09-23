#!/usr/bin/python3
"""
Module defining a custom list class with a method to print the list in sorted order.

Classes:
    Mylist: Inherits from list and adds a method to print the list sorted.

Methods:
    print_sorted(self): Prints the list in sorted order.
"""

class Mylist(list):
    """
    Custom list class with an additional method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.

        This method sorts the list and prints the sorted list.
        """
        print(sorted(self))