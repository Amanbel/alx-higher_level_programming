#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        cp_list = my_list.copy()
        if idx >= len(my_list) or idx < 0:
            cp_list.insert(idx, element)

        return cp_list
