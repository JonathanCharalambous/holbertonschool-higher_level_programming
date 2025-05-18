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
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
