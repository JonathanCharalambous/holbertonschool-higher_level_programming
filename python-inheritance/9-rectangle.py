#!/usr/bin/python3
"""
This module defines a class that is
used to represent a Rectangle which implements BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """"
    class that is used to represent
    a Rectangle which implements BaseGeometry
    """""
    def __init__(self, width, height):
        """Initializes the Rectangle class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height
    
    def print(self):
        """Prints the rectangle."""
        print("{} / {}".format(self.__width, self.__height))

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)