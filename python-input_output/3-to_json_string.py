#!/usr/bin/python3
import json
"""
This module provides the to_json_string function that
converts an object to its JSON string representation
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
