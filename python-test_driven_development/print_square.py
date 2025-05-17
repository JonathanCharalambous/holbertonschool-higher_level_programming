#!/usr/bin/python3

def print_square(size):

    if not isinstance(size, int):
        raise TypeError("Size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")
    

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()