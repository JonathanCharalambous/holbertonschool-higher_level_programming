#!/usr/bin/python3
"""
This module provides the from_json_string function that
converts a JSON string to its corresponding Python data structure
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
