#!/usr/bin/python3

def uppercase(c):
    result = []
    for ch in c:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        else:
            result.append(ch)
    print("{}".format(''.join(result)), end='')
