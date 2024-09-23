#!/usr/bin/python3
class MyList(list):
    """
    MyList inherits from list and provides an additional method to print the list in sorted order.
    """


    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
