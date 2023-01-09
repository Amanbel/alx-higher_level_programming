#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if (my_list == []):
            print("{:d}".format(0))
            break
        print("{:d}".format(i))
