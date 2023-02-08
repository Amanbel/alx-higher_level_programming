#!/usr/bin/python3
"""module function"""


class Student:
    """class of student"""
    def __init__(self, first_name, last_name, age):
        """initializer function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary of instanciated object attributes"""
        return self.__dict__
