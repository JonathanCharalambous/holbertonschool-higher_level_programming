#!/usr/bin/python3

"""
This module defines an empty class Rectangle that is
used to represent a rectangle.
"""


class Rectangle:

    """This class defines a blank Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)

    def print(self):
        """Prints the rectangle with the character #"""
        for i in range(self.__height):
            for i in range(self.__width):
                print("{}".format(Rectangle.print_symbol), end="")
            print()

    def __str__(self):
        """Prints the rectangle with the character #"""
        symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a messages when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greater area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
