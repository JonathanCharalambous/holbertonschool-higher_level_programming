#!/usr/bin/python3
"""
This module provides the class_to_json function that
converts a Python object to its JSON representation
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__