#!/usr/bin/python3
import json
"""
This module provides the from_json_string function that
converts a JSON string to its corresponding Python data structure
"""


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
