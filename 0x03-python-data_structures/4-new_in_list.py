#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return None

    cp_list = my_list.copy()

    return cp_list.insert(idx, element)
