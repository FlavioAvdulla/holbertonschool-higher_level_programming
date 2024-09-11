#!/usr/bin/python3

"""
Script Documentation

Overview:
This Python script defines a function `multiply_list_map` that takes a list of integers and a number, and returns a new list with each element in the original list multiplied by the given number. The function uses the `map` function and a lambda expression to achieve this without using any loops.

Function:
- multiply_list_map(my_list=[], number=0):
    - Parameters:
        - my_list: A list of integers. Defaults to an empty list.
        - number: An integer by which each element in `my_list` will be multiplied. Defaults to 0.
    - Returns:
        - A new list with each element in `my_list` multiplied by `number`.

Logic:
1. Use the `map` function with a lambda expression to multiply each element in `my_list` by `number`.
2. Convert the result of `map` to a list and return it.
"""

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
