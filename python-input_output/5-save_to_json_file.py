#!/usr/bin/python3
import json
"""
This module provides the from_json_string function that
converts a JSON string to its corresponding Python data structure
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)

