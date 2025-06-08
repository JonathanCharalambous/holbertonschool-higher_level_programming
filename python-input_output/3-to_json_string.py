#!/usr/bin/python3
"""
This module provides the to_json_string function that
converts an object to its JSON string representation
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
