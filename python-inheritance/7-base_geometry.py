#!/usr/bin/python3
"""
This module defines a class that is
used to represent BaseGeometry.
"""


class BaseGeometry:
    """A class BaseGeometry."""
    def __init__(self):
        """Initializes the BaseGeometry class."""
        pass

    def area(self):
        """Calculates the area of a geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
