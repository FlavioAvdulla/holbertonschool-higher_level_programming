#!/usr/bin/python3
"""
This module defines a MyList class that extends the built-in list class.

Classes:
    Defines MyList, a subclass of list with a method to print the list sorted.
"""


class MyList(list):
    """
    A list subclass with a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list.
        """
        print(sorted(self))
