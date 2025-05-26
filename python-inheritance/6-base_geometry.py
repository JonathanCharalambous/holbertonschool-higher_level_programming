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
        raise Exception("area() is not implemented ")
