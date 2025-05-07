#!/usr/bin/python3
letter = 'a'
for i in range(26):
    if letter != 'e' and letter != 'q':
        print(letter, end='')
    letter = chr(ord(letter) + 1)    
    