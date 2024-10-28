# Python - Serialization

## Introduction

Welcome to our exploration of marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.

## Table of Contents

1. [Basic Serialization](#basic-serialization)
2. [Pickling Custom Classes](#pickling-custom-classes)
3. [Converting CSV Data to JSON Format](#converting-csv-data-to-json-format)
4. [Serializing and Deserializing with XML](#serializing-and-deserializing-with-xml)

## Basic Serialization

Write a Python module named `task_00_basic_serialization.py` with the following functions:

- **serialize_and_save_to_file(data, filename)**: Takes a Python Dictionary with data and the filename of the output JSON file. If the output file already exists, it should be replaced.
- **load_and_deserialize(filename)**: Takes the filename of the input JSON file and returns a Python Dictionary with the deserialized JSON data from the file.

File: [task_00_basic_serialization.py](task_00_basic_serialization.py)

## Pickling Custom Classes

Learn how to serialize and deserialize custom Python objects using the pickle module.

1. Create a custom Python class named `CustomObject` with the following attributes:
    - `name` (a string)
    - `age` (an integer)
    - `is_student` (a boolean)
    - Additionally, the class should have a method `display` to print out the object’s attributes.
2. Implement two methods within this class:
    - `serialize(self, filename)`: Takes a filename as its parameter. Using the pickle module, it serializes the current instance of the object and saves it to the provided filename.
    - `deserialize(cls, filename)`: A class method that takes a filename as its parameter. Using the pickle module, it loads and returns an instance of the `CustomObject` from the provided filename.
3. Save your code in a file named `task_01_pickle.py`. Handle possible exceptions for non-existent or malformed files. If this happens, the methods should return `None`.

File: [task_01_pickle.py]task_01_pickle.py

## Converting CSV Data to JSON Format

Gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

1. Import the required modules:
    ```python
    import csv
    import json
    ```
2. Define a function named `convert_csv_to_json` that takes the CSV filename as its parameter and writes the JSON data to `data.json`.
3. Inside this function:
    - Use Python’s csv module to open the CSV file and read the data. Use the `DictReader` class to convert each row into a dictionary.
    - Serialize the list of dictionaries using the json module.
    - Write the serialized JSON data to `data.json`.
4. The function should return `True` if the conversion was successful.
5. Handle exceptions, such as file not found. The function should return `False` in this case.
6. Save your work in `task_02_csv.py`.

File: [task_02_csv.py](task_02_csv.py)

## Serializing and Deserializing with XML

Explore serialization and deserialization using XML as an alternative format to JSON.

1. Import the required modules. You can use the `xml.etree.ElementTree` module which is a part of Python’s standard library for XML processing:
    ```python
    import xml.etree.ElementTree as ET
    ```
2. Define two main functions:
    - **serialize_to_xml(dictionary, filename)**: Takes a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.
    - **deserialize_from_xml(filename)**: Takes a filename as its parameter, reads the XML data from that file, and returns a deserialized Python dictionary.
3. For `serialize_to_xml`:
    - Create a root element, e.g., `<data>`.
    - Iterate through the dictionary items and add them as child elements to the root.
    - Write the XML tree to the provided filename using the `ET.ElementTree` class.
4. For `deserialize_from_xml`:
    - Parse the XML file using `ET.parse`.
    - Navigate through the XML elements to reconstruct the dictionary.
    - Return the constructed dictionary.
5. Be cautious about data types. XML doesn’t differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.
6. Save your work in `task_03_xml.py`.

File: [task_03_xml.py](task_03_xml.py)
