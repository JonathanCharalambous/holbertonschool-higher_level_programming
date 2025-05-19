#!/usr/bin/python3

"""
This module defines an empty class Rectangle that is
used to represent a rectangle.
"""


class Rectangle:

    """This class defines a blank Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Getter for Rectangle.width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Rectangle.width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for Rectangle.height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter for Rectangle.height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area for a Rectangle"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """Returns the area for a Rectangle"""
        return (self.__width * 2 + self.__height * 2)
