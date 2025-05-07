#!/usr/bin/python3

for i in range(10):
    for j in range(1, 10):
        num1 = i
        num2 = j
        if num1 < num2:
            print("{}{}".format(num1, num2), end=", " if not (num1 == 8 and num2 == 9) else "\n")
