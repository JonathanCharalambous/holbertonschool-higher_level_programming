#!/usr/bin/python3
"""
This module provides the append_write function that
appends to a text file (UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
