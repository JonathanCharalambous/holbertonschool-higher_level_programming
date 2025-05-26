#!/usr/bin/python3
"""
This module defines a function that is
used to return a sorted list.
"""


class MyList(list):

    """A class of list that includes a method to print sorted."""
    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(self))