#!/usr/bin/python3
"""
This module defines a class that is
used to represent a Square which implements Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """"
    class that is used to represent
    a Square which implements Rectangle
    """""
    def __init__(self, size):
        """Initializes the Square class."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size
