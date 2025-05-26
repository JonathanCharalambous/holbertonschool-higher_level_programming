#!/usr/bin/python3
"""
This module defines a function that is
used to check if a class is an instance of a specified class.
"""

def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if it is an instance of a class that inherited from, a specified class."""
    return isinstance(obj, a_class)
