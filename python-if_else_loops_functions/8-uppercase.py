#!/usr/bin/python3

def uppercase(c):
    for i in range(len(c)):
        if ord(c[i]) >= 97 and ord(c[i]) <= 122:
            c = c[:i] + chr(ord(c[i]) - 32) + c[i + 1:]
    print("{}".format(c), end='\n')
