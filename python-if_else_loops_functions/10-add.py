#!/usr/bin/python3
def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a + b

add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
print(add(-100, -2))
print(add(0, 0))

try:
    print(add(98, "Holberton"))
except TypeError as e:
    print(e)
