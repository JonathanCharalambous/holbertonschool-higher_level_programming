#!/usr/bin/python3
"""
This module defines a function that is
used to check if a class is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specified class."""
    return type(obj) is a_class