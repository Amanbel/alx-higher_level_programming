#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    map(lambda x: x if my_list.count(x) == 1 else my_list.pop(my_list.index(x)), my_list)
    for i in my_list:
        res += i
    return res
