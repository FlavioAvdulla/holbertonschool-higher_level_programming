# python-classes

## Table of Contents
1. My First Square
2. Square with Size
3. Size Validation
4. Area of a Square
5. Access and Update Private Attribute
6. Printing a Square
7. Coordinates of a Square

## My First Square
**File:** [0-square.py](0-square.py)

## Square with Size
**File:** [1-square.py](1-square.py)

## Size Validation
**File:** [2-square.py](2-square.py)

## Area of a Square
**File:** [3-square.py](3-square.py)

## Access and Update Private Attribute
**File:** [4-square.py](4-square.py)

## Printing a Square
**File:** [5-square.py](5-square.py)

## Coordinates of a Square
**File:** [6-square.py](6-square.py)

## Class Square
Write a class `Square` that defines a square by: (based on `5-square.py`)

- **Private instance attribute: `size`:**
  - `property def size(self):` to retrieve it
  - `property setter def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
- **Private instance attribute: `position`:**
  - `property def position(self):` to retrieve it
  - `property setter def position(self, value):` to set it:
    - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- **Instantiation with optional `size` and optional `position`:** `def __init__(self, size=0, position=(0, 0)):`
- **Public instance method:** `def area(self):` that returns the current square area
- **Public instance method:** `def my_print(self):` that prints in stdout the square with the character `#`:
  - if `size` is equal to 0, print an empty line
  - `position` should be used by using space - Don’t fill lines by spaces when `position[1] > 0`
- You are not allowed to import any module
