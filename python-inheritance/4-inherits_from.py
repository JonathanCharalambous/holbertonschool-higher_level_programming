#!/usr/bin/python3
"""
This module defines a function that is
used to check if a class is an instance of a class that
inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that
    inherited (directly or indirectly) from a specified class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
