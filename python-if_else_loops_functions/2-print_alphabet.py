#!/usr/bin/python3
letter = 'a'
for i in range(26):
    print(letter, end='')
    letter = chr(ord(letter) + 1)
    