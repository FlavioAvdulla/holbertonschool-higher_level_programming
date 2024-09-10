#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to check which elements in a list are divisible by 2.

The script imports the `divisible_by_2` function from the module named '10-divisible_by_2'.
It then creates a list of integers and uses the imported function to generate a list of boolean values indicating whether each element is divisible by 2.
Finally, it iterates through the list and prints whether each element is divisible by 2.

Example:
    $ ./import_and_check_divisibility.py
    0 is divisible by 2
    1 is not divisible by 2
    2 is divisible by 2
    3 is not divisible by 2
    4 is divisible by 2
    5 is not divisible by 2
    6 is divisible by 2
"""

divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
