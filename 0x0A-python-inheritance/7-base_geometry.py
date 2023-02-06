#!/usr/bin/python3
"""class names BaseGeometry"""


class BaseGeometry:
    """base class for geometry"""

    def area(self):
        """calculates area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates input integer"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
