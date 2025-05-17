#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for num in my_list:
            print(num, end="")
            count += 1
    except (TypeError, ValueError):
        pass
    except IndexError:
        pass
    print()
    return count