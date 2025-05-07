#!/usr/bin/python3
output = ""
for i in range(99):
    output += "{} = {}\n".format(i, hex(i))
print(output, end='')
