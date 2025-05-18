#!/usr/bin/python3
    """
    This module provides the say_my_name function that
    prints a message with the provided strings.
    """
def print_square(size):
    """
    Prints a message with the two provided arguments.

    Args:
        first_name: First name to print.
        last_name: Last name to print.

    Returns:
        No return

    Raises:
        TypeError: If first name is not a string.
        TypeError: Iflast name is not a string.

    """
    if not isinstance(size, int):
        raise TypeError("Size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")
    

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
