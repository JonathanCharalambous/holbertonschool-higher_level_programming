#!/usr/bin/python3
"""
This module provides the text_indentation function that
a provided text with indentations added.
"""


def text_indentation(text):
    """
    Prints a provided text with indentations added.

    Args:
        text: The text to indent.

    Returns:
        No return

    Raises:
        TypeError: If text is not an string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for letter in text:
        print(letter, end="")
        if letter in ".?:":
            print()
            print()
