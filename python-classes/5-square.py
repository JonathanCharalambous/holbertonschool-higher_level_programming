#!/usr/bin/python3
"""
    This module defines a class Square used to represent a square.
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

    @property
    def size(self):
        """Getter for square.size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for square.size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Prints a square using # based on size."""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()