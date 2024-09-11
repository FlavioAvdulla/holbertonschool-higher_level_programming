#!/usr/bin/python3

"""
Script Documentation

Overview:
This Python script imports the `multiply_list_map` function from the `11-multiply_list_map` module and uses it to multiply each element in a list by a given number. It then prints the new list and the original list to demonstrate that the original list remains unchanged.

Modules Used:
- 11-multiply_list_map: This module contains the `multiply_list_map` function.

Variables:
- my_list: A list of integers to be multiplied.
- new_list: A new list containing the results of multiplying each element in `my_list` by the given number.

Functions:
- multiply_list_map(my_list, number): Returns a new list with each element in `my_list` multiplied by `number`.

Logic:
1. Import the `multiply_list_map` function from the `11-multiply_list_map` module.
2. Define a list `my_list` with sample data.
3. Call the `multiply_list_map` function with `my_list` and a multiplier (4) and store the result in `new_list`.
4. Print `new_list` to show the multiplied values.
5. Print `my_list` to show that the original list remains unchanged.
"""

multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

# Define a list with sample data
my_list = [1, 2, 3, 4, 6]

# Multiply each element in the list by 4 and store the result in a new list
new_list = multiply_list_map(my_list, 4)

# Print the new list with multiplied values
print(new_list)

# Print the original list to show it remains unchanged
print(my_list)
