# Rectangle Class Tasks

## Table of Contents
1. Simple Rectangle
2. Real Definition of a Rectangle
3. Area and Perimeter
4. String Representation
5. Eval is Magic
6. Detect Instance Deletion
7. How Many Instances
8. Change Representation
9. Compare Rectangles
10. A Square is a Rectangle

## Simple Rectangle
**File:** [0-rectangle.py](0-rectangle.py)

## Real Definition of a Rectangle
**File:** [1-rectangle.py](1-rectangle.py)

## Area and Perimeter
**File:** [2-rectangle.py](2-rectangle.py)

## String Representation
**File:** [3-rectangle.py](3-rectangle.py)

## Eval is Magic
**File:** [4-rectangle.py](4-rectangle.py)

## Detect Instance Deletion
**File:** [5-rectangle.py](5-rectangle.py)

## How Many Instances
**File:** [6-rectangle.py](6-rectangle.py)

## Change Representation
**File:** [7-rectangle.py](7-rectangle.py)

## Compare Rectangles
**File:** [8-rectangle.py](8-rectangle.py)

## A Square is a Rectangle
**File:** [9-rectangle.py](9-rectangle.py)

## Class Rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

- **Private instance attribute: `width`:**
  - `property def width(self):` to retrieve it
  - `property setter def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- **Private instance attribute: `height`:**
  - `property def height(self):` to retrieve it
  - `property setter def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- **Public class attribute `number_of_instances`:**
  - Initialized to 0
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- **Public class attribute `print_symbol`:**
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- **Instantiation with optional `width` and `height`:** `def __init__(self, width=0, height=0):`
- **Public instance method:** `def area(self):` that returns the rectangle area
- **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to 0, perimeter has to be equal to 0
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- **Static method** `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  - Returns `rect_1` if both have the same area value
- **Class method** `def square(cls, size=0):` that returns a new `Rectangle` instance with `width == height == size`
- You are not allowed to import any module
