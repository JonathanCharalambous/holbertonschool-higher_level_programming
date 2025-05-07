#!/usr/bin/python3
num = 0
for i in range(100):
    if num < 99:
        print(f"{num:02d}, ", end='')
    else:
        print(f"{num:02d}")
    num += 1
    