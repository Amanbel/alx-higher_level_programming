#!/usr/bin/python3
"""module with a class of Rectangle"""


class BaseGeometry:
    """beta version of a class"""
    def area(self):
        """area calculator"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates input integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))



class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        """initalizing function"""
        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)
        self.__width = width
        self.__height = height
