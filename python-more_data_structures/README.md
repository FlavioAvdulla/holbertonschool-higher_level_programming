# Python Functions for Various Tasks

This repository contains a collection of Python functions designed to perform various tasks. Each task is implemented in a separate Python file.

## Table of Contents

1. Squared Simple
2. Search and Replace
3. Unique Addition
4. Present in Both
5. Only Differents
6. Number of Keys
7. Print Sorted Dictionary
8. Update Dictionary
9. Simple Delete by Key
10. Multiply by 2
11. Best Score
12. Multiply by Using Map
13. Roman to Integer

## Squared Simple

**File:** [0-square_matrix_simple.py](0-square_matrix_simple.py)

Write a function that computes the square value of all integers in a matrix.

### Requirements:
- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
    - Same size as `matrix`
    - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, `map`, etc.

## Search and Replace

**File:** [1-search_replace.py](1-search_replace.py)

Write a function that replaces all occurrences of an element by another in a new list.

### Requirements:
- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- You are not allowed to import any module

## Unique Addition

**File:** [2-uniq_add.py](2-uniq_add.py)

Write a function that adds all unique integers in a list (only once for each integer).

### Requirements:
- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any module

## Present in Both

**File:** [3-common_elements.py](3-common_elements.py)

Write a function that returns a set of common elements in two sets.

### Requirements:
- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module

## Only Differents

**File:** [4-only_diff_elements.py](4-only_diff_elements.py)

Write a function that returns a set of all elements present in only one set.

### Requirements:
- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any module

## Number of Keys

**File:** [5-number_keys.py](5-number_keys.py)

Write a function that returns the number of keys in a dictionary.

### Requirements:
- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module

## Print Sorted Dictionary

**File:** [6-print_sorted_dictionary.py](6-print_sorted_dictionary.py)

Write a function that prints a dictionary by ordered keys.

### Requirements:
- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module

## Update Dictionary

**File:** [7-update_dictionary.py](7-update_dictionary.py)

Write a function that replaces or adds key/value in a dictionary.

### Requirements:
- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string
- `value` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are not allowed to import any module

## Simple Delete by Key

**File:** [8-simple_delete.py](8-simple_delete.py)

Write a function that deletes a key in a dictionary.

### Requirements:
- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will be always a string
- If a key doesn’t exist, the dictionary won’t change
- You are not allowed to import any module

## Multiply by 2

**File:** [9-multiply_by_2.py](9-multiply_by_2.py)

Write a function that returns a new dictionary with all values multiplied by 2.

### Requirements:
- Prototype: `def multiply_by_2(a_dictionary):`
- You can assume that all values are only integers
- Returns a new dictionary
- You are not allowed to import any module

## Best Score

**File:** [10-best_score.py](10-best_score.py)

Write a function that returns a key with the biggest integer value.

### Requirements:
- Prototype: `def best_score(a_dictionary):`
- You can assume that all values are only integers
- If no score found, return `None`
- You can assume all students have a different score
- You are not allowed to import any module

## Multiply by Using Map

**File:** [11-multiply_list_map.py](11-multiply_list_map.py)

Write a function that returns a list with all values multiplied by a number without using any loops.

### Requirements:
- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list:
    - Same length as my_list
    - Each value should be multiplied by `number`
- Initial list should not be modified
- You are not allowed to import any module
- You have to use `map`
- Your file should be max 3 lines

## Roman to Integer

**File:** [12-roman_to_int.py](12-roman_to_int.py)

Create a function `def roman_to_int(roman_string):` that converts a [Roman numeral](https://en.wikipedia.org/wiki/Roman_numerals) to an integer.

### Requirements:
- You are not allowed to google anything
- Whiteboard first
- You can assume the number will be between 1 to 3999.
- `def roman_to_int(roman_string)` must return an integer
- If the `roman_string` is not a string or `None`, return 0
