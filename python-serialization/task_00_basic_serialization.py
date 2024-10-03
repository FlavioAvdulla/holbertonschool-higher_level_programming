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
    with open('filename', 'w') as file:
        json.dump(data, file)
    print(f"Data serialised and saved to: {filename}.")


def load_and_deserialize(filename):
    with open('filename', 'r') as file:
        data = json.load(file)
    return data


serialize_and_save_to_file(data_to_serialize, 'data.json')
load_and_deserialize('data.json')
