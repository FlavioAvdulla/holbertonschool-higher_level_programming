# Python Import and Function Projects

This repository contains several Python scripts that demonstrate importing functions from different files and performing various operations. Each script is designed to fulfill specific requirements as outlined below.

## Table of Contents
1. Import a Simple Function
2. My First Toolbox
3. How to Make a Script Dynamic
4. Infinite Addition
5. Who Are You?
6. Everything Can Be Imported
7. Read File
8. Write to a File
9. Append to a File
10. To JSON String
11. From JSON String to Object
12. Save Object to a File
13. Create Object from a JSON File
14. Load, Add, Save
15. Class to JSON
16. Student to JSON

## Import a Simple Function
**File:** 0-add.py

This script imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

### Requirements:
- Use the `print` function with string format to display integers.
- Assign the value `1` to a variable called `a`.
- Assign the value `2` to a variable called `b`.
- Use these two variables as arguments when calling the functions `add` and `print`.
- `a` and `b` must be defined in 2 different lines: `a = 1` and `b = 2`.
- The program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
- Only use the word `add_0` once in your code.
- Do not use `*` for importing or `__import__`.
- The code should not be executed when imported.

## My First Toolbox
**File:** 1-calculation.py

This script imports functions from the file `calculator_1.py`, performs some mathematical operations, and prints the results.

### Requirements:
- Do not use the `print` function (with string format to display integers) more than 4 times.
- Assign the value `10` to a variable `a`.
- Assign the value `5` to a variable `b`.
- Use these two variables only as arguments when calling functions (including `print`).
- `a` and `b` must be defined in 2 different lines: `a = 10` and `b = 5`.
- The script should call each of the imported functions.
- Only use the word `calculator_1` once in your file.
- Do not use `*` for importing or `__import__`.
- The code should not be executed when imported.

## How to Make a Script Dynamic
**File:** 2-args.py

This script prints the number of and the list of its arguments.

### Requirements:
- The output should be:
  - `Number of argument(s)` followed by `argument` (if the number is one) or `arguments` (otherwise), followed by `:` (or `.` if no arguments were passed), followed by a new line.
  - If at least one argument is passed, print one line per argument: the position of the argument (starting at 1) followed by `:`, followed by the argument value and a new line.
- The code should not be executed when imported.
- The number of elements of `argv` can be retrieved by using: `len(argv)`.

## Infinite Addition
**File:** 3-infinite_add.py

This script prints the result of the addition of all arguments.

### Requirements:
- The output should be the result of the addition of all arguments, followed by a new line.
- You can cast arguments into integers by using `int()` (you can assume that all arguments can be cast into integers).
- The code should not be executed when imported.

## Who Are You?
**File:** 4-hidden_discovery.py

This script prints all the names defined by the compiled module `hidden_4.pyc`.

### Requirements:
- This task must be done on the sandbox only.
- The file `4-hidden_discovery.py` must be located in the folder `/tmp/`.
- Print one name per line, in alphabetical order.
- Print only names that do not start with `__`.
- The code should not be executed when imported.

## Everything Can Be Imported
**File:** 5-variable_load.py

This script imports the variable `a` from the file `variable_load_5.py` and prints its value.

### Requirements:
- Do not use `*` for importing or `__import__`.
- The code should not be executed when imported.

## Read File
**File:** 0-read_file.py

Write a function that reads a text file (UTF8) and prints it to stdout.

### Requirements:
- Prototype: `def read_file(filename=""):`
- You must use the `with` statement.
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module.

## Write to a File
**File:** 1-write_file.py

Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

### Requirements:
- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement.
- You don’t need to manage file permission exceptions.
- Your function should create the file if it doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module.

## Append to a File
**File:** 2-append_write.py

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

### Requirements:
- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created.
- You must use the `with` statement.
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module.

## To JSON String
**File:** 3-to_json_string.py

Write a function that returns the JSON representation of an object (string).

### Requirements:
- Prototype: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.

## From JSON String to Object
**File:** 4-from_json_string.py

Write a function that returns an object (Python data structure) represented by a JSON string.

### Requirements:
- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

## Save Object to a File
**File:** 5-save_to_json_file.py

Write a function that writes an Object to a text file, using a JSON representation.

### Requirements:
- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement.
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.

## Create Object from a JSON File
**File:** 6-load_from_json_file.py

Write a function that creates an Object from a “JSON file”.

### Requirements:
- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement.
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.

## Load, Add, Save
**File:** 7-add_item.py

Write a script that adds all arguments to a Python list, and then save them to a file.

### Requirements:
- You must use your function `save_to_json_file` from `5-save_to_json_file.py`.
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`.
- The list must be saved as a JSON representation in a file named `add_item.json`.
- If the file doesn’t exist, it should be created.
- You don’t need to manage file permissions / exceptions.

## Class to JSON
**File:** 8-class_to_json.py

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

### Requirements:
- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class.
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean.
- You are not allowed to import any module.