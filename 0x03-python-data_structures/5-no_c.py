#!/usr/bin/python3
def no_c(my_string):
    new = ""
    if my_string:
        for i in my_string:
            if i is not 'c' and i is not 'C':
                new += i
    return new
