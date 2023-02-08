#!/usr/bin/python3
"""module for a class"""


class Student:
    """class for student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a specific dictionary"""
        dicts = {}
        for key in attrs:
            if key in self.__dict__:
                dicts[key] = get(key)
            else:
                pass
        return dicts
