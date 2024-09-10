#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to print a matrix of integers.

The script imports the `print_matrix_integer` function from the module named '6-print_matrix_integer'.
It then creates a matrix (a list of lists) and uses the imported function to print each row of the matrix.
Finally, it prints a separator line and calls the function again with the default empty matrix.

Example:
    $ ./import_and_print_matrix.py
    1 2 3
    4 5 6
    7 8 9
    --
"""
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
