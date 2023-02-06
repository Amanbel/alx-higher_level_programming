#!/usr/bin/python3
"""module with a single function"""


def inherits_from(obj, a_class):
    """checks if obj inherits from a_class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
