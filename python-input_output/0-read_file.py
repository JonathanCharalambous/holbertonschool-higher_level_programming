#!/usr/bin/python3
"""
This module provides the read_file function that
Reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
