#!/usr/bin/python3
"""module that has only one function"""


def is_same_class(obj, a_class):
    """functions that checks if an object is related to a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
