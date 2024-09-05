#!/usr/bin/python3
def add(a, b):
    if type(a) is not int:
        a = 0
    if type(b) is not int:
        b = 0
    return a + b

add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
