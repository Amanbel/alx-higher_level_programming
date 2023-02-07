#!/usr/bin/python3
"""function module"""


def add_attribute(instance, name_attr, value_attr):
    """function that sets a new attribut to an object instance"""
    if isinstance(instance, str) or isinstance(instance, int) or isinstance(instance, float) or isinstance(instance, bool):
        raise TypeError("can't add new attribute")
    else:
        setattr(instance, name_attr, value_attr)
