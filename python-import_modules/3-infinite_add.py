#!/usr/bin/python3
from sys import argv

sum = 0

for i in range(1, len(argv)):
    sum += int(argv[i])
print("{}".format(sum))

if __name__ == "__main__":
    main()
