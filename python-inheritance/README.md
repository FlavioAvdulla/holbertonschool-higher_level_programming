# Python - Inheritance

## Table of Contents
1. Lookup
2. My List
3. Exact Same Object
4. Same Class or Inherit From
5. Only Sub Class Of
6. Geometry Module
7. Improve Geometry
8. Integer Validator
9. Rectangle
10. Full Rectangle
11. Square #1
12. Square #2

## 0. Lookup
Write a function that returns the list of available attributes and methods of an object:

- Prototype: `def lookup(obj):`
- Returns a list object
- You are not allowed to import any module

File: [0-lookup.py](0-lookup.py)

## 1. My List
Write a class `MyList` that inherits from `list`:

- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type `int`
- You are not allowed to import any module

Files: [1-my_list.py](1-my_list.py), [tests/1-my_list.txt](tests/1-my_list.txt)

## 2. Exact Same Object
Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

- Prototype: `def is_same_class(obj, a_class):`
- You are not allowed to import any module

File: [2-is_same_class.py](2-is_same_class.py)

## 3. Same Class or Inherit From
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

- Prototype: `def is_kind_of_class(obj, a_class):`
- You are not allowed to import any module

File: [3-is_kind_of_class.py](3-is_kind_of_class.py)

## 4. Only Sub Class Of
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

- Prototype: `def inherits_from(obj, a_class):`
- You are not allowed to import any module

File: [4-inherits_from.py](4-inherits_from.py)

## 5. Geometry Module
Write an empty class `BaseGeometry`.

- You are not allowed to import any module

File: [5-base_geometry.py](5-base_geometry.py)

## 6. Improve Geometry
Write a class `BaseGeometry` (based on `5-base_geometry.py`).

- Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
- You are not allowed to import any module

File: [6-base_geometry.py](6-base_geometry.py)

## 7. Integer Validator
Write a class `BaseGeometry` (based on `6-base_geometry.py`).

- Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
- Public instance method: `def integer_validator(self, name, value):` that validates `value`:
  - You can assume `name` is always a string
  - If `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
  - If `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
- You are not allowed to import any module

Files: [7-base_geometry.py](7-base_geometry.py), [tests/7-base_geometry.txt](tests/7-base_geometry.txt)

## 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

- Instantiation with `width` and `height`: `def __init__(self, width, height):`
  - `width` and `height` must be private. No getter or setter
  - `width` and `height` must be positive integers, validated by `integer_validator`

File: [8-rectangle.py](8-rectangle.py)

## 9. Full Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

- Instantiation with `width` and `height`: `def __init__(self, width, height):`
  - `width` and `height` must be private. No getter or setter
  - `width` and `height` must be positive integers validated by `integer_validator`
- The `area()` method must be implemented
- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

File: [9-rectangle.py](9-rectangle.py)

## 10. Square #1
Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

- Instantiation with `size`: `def __init__(self, size):`
  - `size` must be private. No getter or setter
  - `size` must be a positive integer, validated by `integer_validator`
- The `area()` method must be implemented

File: [10-square.py](10-square.py)

## 11. Square #2
Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

- Instantiation with `size`: `def __init__(self, size):`
  - `size` must be private. No getter or setter
  - `size` must be a positive integer, validated by `integer_validator`
- The `area()` method must be implemented
- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

File: [11-square.py](11-square.py)
