#!/usr/bin/python3
def add(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("Both arguments must be integers")
    return a + b
