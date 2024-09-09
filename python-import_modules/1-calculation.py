#!/usr/bin/python3
"""
This script performs basic arithmetic operations (addition, subtraction,
multiplication, and division) on two numbers and prints the results.

The numbers to be operated on are defined within the script.
"""

from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    pass
