#!/usr/bin/python3
"""
Module for JSON serialization and deserialization.

Functions:
- serialize_and_save_to_file(data, filename):
Serialize a dictionary to a JSON file.
- load_and_deserialize(filename): Deserialize a
JSON file to a dictionary.
"""


import json

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Parameters:
    data (dict): The Python dictionary to serialize.
    filename (str): The filename of the output
    JSON file. If the file exists, it will be replaced.
    """
    with open('filename', 'w') as file:
        """
    Load and deserialize a JSON file to a Python dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
        json.dump(data, file)
    print(f"Data serialised and saved to: {filename}.")


def load_and_deserialize(filename):
    with open('filename', 'r') as file:
        data = json.load(file)
    return data
