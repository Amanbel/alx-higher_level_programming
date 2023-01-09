#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for i in my_list:
            if (my_list == []):
                print("{:d}".format(0))
                break
            print("{:d}".format(i))
