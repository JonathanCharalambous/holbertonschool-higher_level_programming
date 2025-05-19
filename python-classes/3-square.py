#!/usr/bin/python3
"""
This module defines an empty class Square used to represent a square.
"""


class Square:

    """This class defines a square."""
    def __init__(self, size=0):
        """Initialize a new Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Calculate and return the current square area."""
        return (self.__size ** 2)
