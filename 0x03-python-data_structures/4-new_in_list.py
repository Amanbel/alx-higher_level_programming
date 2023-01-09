#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list[:]
    if idx < len(my_list) and idx >= 0:
        cp_list[idx] = element

    return cp_list
