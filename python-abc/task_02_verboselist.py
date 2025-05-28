#!/usr/bin/env python3
"""
This module defines an VerboseList class 
for a list and prints messages with actions pulled
from the super class.
"""


class VerboseList(list):
    """A list that prints messages when items are added or removed."""

    def append(self, item):
        """Append an item to the list and print a message."""
        super().append(item)
        print("Appended {} to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with items from an iterable and print a message."""
        super().extend(iterable)
        print("Extended the list with {}.".format(list(iterable)))

    def remove(self, item):
        """Remove an item from the list and print a message."""
        super().remove(item)
        print("Removed {} from the list.".format(item))
    
    def pop(self, index=-1):
        """Pop an item from the list at the given index and print a message."""
        item = super().pop(index)
        print("Popped {} from the list.".format(item))
        return item