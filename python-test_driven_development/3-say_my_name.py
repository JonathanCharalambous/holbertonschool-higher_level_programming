#!/usr/bin/python3
"""
This module provides the say_my_name function that
prints a message with the provided strings.
"""


def say_my_name(first_name, last_name=""):
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
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
