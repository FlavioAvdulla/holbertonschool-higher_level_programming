#!/usr/bin/python3
"""
This script prints the number of command-line arguments passed to it and lists each argument.

Modules:
    sys: Provides access to command-line arguments.

Functions:
    main(): The main function that processes and prints the command-line arguments.

Usage:
    Run this script from the command line with any number of arguments.
    Example:
        $ ./script_name.py arg1 arg2 arg3

    Output:
        - If no arguments are passed, it prints "0 arguments."
        - If one argument is passed, it prints "1 argument:" followed by the argument.
        - If more than one argument is passed, it prints the number of arguments followed by each argument on a new line.
"""

import sys

def main():
    """
    Processes command-line arguments and prints the number of arguments and each argument.
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
