#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    i = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            i += 1
        except (TypeError, ValueError):
            pass
    print()
    return i
