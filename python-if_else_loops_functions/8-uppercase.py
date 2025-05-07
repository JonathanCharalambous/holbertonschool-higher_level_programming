#!/usr/bin/python3

def uppercase(c):
    if ord('a') <= ord(c) <= ord('z'):
        c = chr(ord(c) - 32)
    print("{}".format(c), end='')
