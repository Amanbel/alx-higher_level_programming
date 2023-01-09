#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0):
        return None
    if (idx >= len(my_list)):
        return None

    ret_ind = my_list[idx, idx + 1]

    return ret_ind
