#!/usr/bin/python3
"""
This script demonstrates the usage of the `square_matrix_simple` function.

The `square_matrix_simple` function takes a matrix (a list of lists of integers)
and returns a new matrix with each element squared.

Example:
    $ ./9-main.py
    [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

# Import the function from the module
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

# Define a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Apply the function to the matrix
new_matrix = square_matrix_simple(matrix)

# Print the new matrix
print(new_matrix)

# Print the original matrix to show it remains unchanged
print(matrix)
