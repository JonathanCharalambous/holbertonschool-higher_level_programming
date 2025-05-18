#!/usr/bin/python3
"""
This module provides the print_square function that
prints a square based on the provided size.
"""
def print_square(size):
    """
    Prints a square based on the provided size.

    Args:
        first_name: First name to print.
        last_name: Last name to print.

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is a negative number.

    """
    if not isinstance(size, int):
        raise TypeError("Size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")
    

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
