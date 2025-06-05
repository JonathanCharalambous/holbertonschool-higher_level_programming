#!/usr/bin/python3
"""
This module provides the write_file function that
writes to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
