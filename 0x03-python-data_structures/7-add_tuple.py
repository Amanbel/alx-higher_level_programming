#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_b) >= 2:
        if len(tuple_a) == 0:
            return tuple_b
        t = (tuple_a[0] + tuple_b[0], tuple_b[1])
        return t
    if len(tuple_b) < 2 and len(tuple_a) >= 2:
        if len(tuple_b) == 0:
            return tuple_a
        t = (tuple_a[0] + tuple_b[0], tuple_a[1])
        return t
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        t = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return t
