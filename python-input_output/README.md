# Python Import and Function Projects

This repository contains several Python scripts that demonstrate importing functions from different files and performing various operations. Each script is designed to fulfill specific requirements as outlined below.

## Table of Contents
1. Read File
2. Write to a File
3. Append to a File
4. To JSON String
5. From JSON String to Object
6. Save Object to a File
7. Create Object from a JSON File
8. Load, Add, Save
9. Class to JSON
10. Student to JSON
11. Student to JSON with Filter
12. Student to Disk and Reload
13. Pascal's Triangle

## Read File
**File:** [0-read_file.py](0-read_file.py)

Write a function that reads a text file (UTF8) and prints it to stdout:

- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

## Write to a File
**File:** [1-write_file.py](1-write_file.py)

Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if it doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

## Append to a File
**File:** [2-append_write.py](2-append_write.py)

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created
- You must use the `with` statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

## To JSON String
**File:** [3-to_json_string.py](3-to_json_string.py)

Write a function that returns the JSON representation of an object (string):

- Prototype: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.

## From JSON String to Object
**File:** [4-from_json_string.py](4-from_json_string.py)

Write a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

## Save Object to a File
**File:** [5-save_to_json_file.py](5-save_to_json_file.py)

Write a function that writes an Object to a text file, using a JSON representation:

- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.

## Create Object from a JSON File
**File:** [6-load_from_json_file.py](6-load_from_json_file.py)

Write a function that creates an Object from a “JSON file”:

- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.

## Load, Add, Save
**File:** [7-add_item.py](7-add_item.py)

Write a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
- The list must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.

## Class to JSON
**File:** [8-class_to_json.py](8-class_to_json.py)

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module

## Student to JSON
**File:** [9-student.py](9-student.py)

Write a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
- You are not allowed to import any module

## Student to JSON with Filter
**File:** [10-student.py](10-student.py)

Write a class `Student` that defines a student by: (based on `9-student.py`)

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
  - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
  - Otherwise, all attributes must be retrieved
- You are not allowed to import any module

## Student to Disk and Reload
**File:** [11-student.py](11-student.py)

Write a class `Student` that defines a student by: (based on `10-student.py`)

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
  - If `attrs` is a list of strings, only attributes name contained in this list must be retrieved.
  - Otherwise, all attributes must be retrieved
- Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
  - You can assume `json` will always be a dictionary
  - A dictionary key will be the public attribute name
  - A dictionary value will be the value of the public attribute
- You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allowing us to rebuild an object based on this representation).

## Pascal's Triangle
**File:** [12-pascal_triangle.py](12-pascal_triangle.py)

Technical interview preparation:

- You are not allowed to google anything
- Whiteboard first

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer
- You are not allowed to import any module
