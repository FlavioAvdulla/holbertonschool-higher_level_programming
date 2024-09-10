#!/usr/bin/python3
"""
This module contains the function `square_matrix_simple`.

The `square_matrix_simple` function takes a matrix (a list of lists of integers)
and returns a new matrix with each element squared.

Function:
    square_matrix_simple(matrix=[])

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
"""

def square_matrix_simple(matrix=[]):
    """
    Computes the square of all integers in a matrix.

    Args:
        matrix (list of list of int): A 2D list where each inner list represents a row of the matrix.

    Returns:
        list of list of int: A new matrix where each element is the square of the corresponding element in the input matrix.
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)
    return new_matrix
