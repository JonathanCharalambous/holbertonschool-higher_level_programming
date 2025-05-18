#!/usr/bin/python3
"""
This module provides the add_integer function that adds two numbers.
"""
def add_integer(a, b=98):
    """
    Adds two numbers, casting them to integers first.

    Args:
        a: The first number
        b: The second number, defaults to 98.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int (b)
