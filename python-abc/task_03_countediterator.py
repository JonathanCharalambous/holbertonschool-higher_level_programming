#!/usr/bin/env python3

class CountedIterator:

    def __init__ (self, iterable):
        """Initialize the iterator with an iterable."""
        self.iterable = iter(iterable)
        self.count = 0
    

    def get_count(self):
        """Return the number of items iterated over."""
        return self.count
    

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        try:
            item = next(self.iterable)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items in the iterator.")
        