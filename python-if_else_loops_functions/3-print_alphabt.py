#!/usr/bin/python3
alphabet = ""
for i in range(ord('a'), ord('z') + 1):
    if i != ord('e') and i != ord('q'):
        alphabet += chr(i)
print("{}".format(alphabet), end='')
