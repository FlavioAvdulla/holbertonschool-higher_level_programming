#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists): A list of lists where each sublist represents a row of the matrix.

    Returns:
        None

    Example:
        >>> print_matrix_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        1 2 3
        4 5 6
        7 8 9
        >>> print_matrix_integer([[10, 20], [30, 40]])
        10 20
        30 40
    """
    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()
