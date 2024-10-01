#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of list of int: A list of lists of integers representing Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0
        return []
    
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            for.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
    return triangle
