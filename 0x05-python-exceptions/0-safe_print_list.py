#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for el in range(0, x):
        try:
            print("{}".format(my_list[el]), end=""))
        except Exception as e:
            break
        else:
            i += 1
    print()
    return i
