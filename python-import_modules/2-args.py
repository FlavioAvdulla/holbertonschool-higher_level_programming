#!/usr/bin/python3
"""
This script counts and lists the command-line arguments passed to it.

It prints the number of arguments and each argument with its index.
"""

import sys


def main():
    """
    Main function to process command-line arguments.

    It counts the number of arguments and prints them in a formatted way.
    """
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
