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
        if attrs is None:
            return self.__dict__
        dicts = {}
        valu = self.__dict__
        for key in attrs:
            if key in valu:
                dicts[key] = valu.get(key)
            else:
                pass
        return dicts

    def reload_from_json(self, json):
        """replaces attributes"""
        self.__dict__.update(json)
