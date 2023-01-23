#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value/2
    except TypeError:
        return False
    else:
        print("{:d}".format(value))
        return True
