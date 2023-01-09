#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    cp_list = my_list.copy()

    if idx >= len(my_list) or idx < 0:
        return cp_list

    return cp_list.insert(idx, element)
