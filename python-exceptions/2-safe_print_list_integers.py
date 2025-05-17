#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    len = x

    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            count += 1
    except (TypeError, ValueError):
        pass
    except IndexError:
        pass
    print()
    return count
