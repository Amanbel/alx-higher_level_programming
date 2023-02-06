#!/usr/bin/python3
"""a module for a function"""


def is_kind_of_class(obj, a_class):
    """function checks if its inherited or not"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
