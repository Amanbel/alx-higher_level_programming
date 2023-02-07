#!/usr/bin/python3
"""function module"""


def add_attribute(inst, name_attr, value_attr):
    """function that sets a new attribut to an object instance"""
    if type(inst) == str or type(inst) == int or type(inst) == float or type(inst) == bool:
        raise TypeError("can't add new attribute")
    else:
        setattr(inst, name_attr, value_attr)
