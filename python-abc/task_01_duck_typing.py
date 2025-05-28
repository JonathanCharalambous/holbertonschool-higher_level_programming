#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math
"""
This module defines an abstract base class 
for shapes and concrete implementations for Circle and Rectangle.
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    """Concrete implementation of Shape for circles."""
    def __init__ (self, radius):
        """Initialize the circle"""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Concrete implementation of Shape for rectangles."""
    def __init__ (self, width, height):
        """Initialize the rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
def shape_info(shape):
    """Print the area and perimeter of the shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
