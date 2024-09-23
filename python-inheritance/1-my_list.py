#!/usr/bin/python3
"""
This module defines a MyList class that extends the built-in list class.

Classes:
    MyList: A subclass of list that includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in list class that includes a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list.
        """
        print(sorted(self))
