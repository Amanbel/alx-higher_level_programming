#!/usr/bin/python3
"""module with single class"""


class BaseGeometry:
    """beta version of a class"""
    def area(self):
        """area calculator"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates input integer"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
