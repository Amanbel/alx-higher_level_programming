#!/usr/bin/python3
"""function module"""


def add_attribute(inst, name_attr, value_attr):
    """function that sets a new attribut to an object instance"""
    if hasattr(inst, "__dict__") or \
            (hasattr(inst, "__slot__") and name_attr in inst.__slot__):
        setattr(inst, name_attr, value_attr)
    else:
        raise TypeError("can't add new attribut")
