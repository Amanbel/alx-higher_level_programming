#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    i = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
        except IndexError:
            raise
        except:
            pass
        else:
            i += 1
    print()
    return i
