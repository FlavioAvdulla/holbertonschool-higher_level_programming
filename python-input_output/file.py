# How to open a file.
file = open('example.txt', 'r') # 'r' (reading) 'w' (writing) 'a'(appending)

# How to write text in a file.
with open('example.txt', 'w') as file:
    file.write('Hello, world!') 

# How to read a file line by line:
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')

# How to make sure a file is closed after using it
with open('example.txt', 'r') as file:
    content = file.read()

# The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks.
with open('example.txt', 'r') as file:
    content = file.read()

# Sertialization: Serialization is the process of converting a Python object into a JSON string.
import json
data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)

# Deserialization: Deserialization is the process of converting a JSON string back into a Python object.
import json
data = {'name': 'John', 'age':30}
json_string = json.dumps(data)

# How to convert a JSON string to a Python Data Structure
import json
json_string = '{"name": "John, "age": 30}'
data = json.loads(json_string)
print(data)

# How to access comand line parameters in a python script
import sys
print(sys.argv)

# Get the current working directory and list all files
import os
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

files_and_dirs = os.listdir(current_directory)
print(f"Files and Directories: {files_and_dirs}")
print()