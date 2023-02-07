#!/usr/bin/python3
"""class module"""


class MyInt(int):
    """subclass of int"""
    def __init__(self, value):
        self.__value = value

    def __new__(cls, *args, **kwargs):
        """new class of int"""
        return super(MyInt, cls).__new__(cls, value + 1)
