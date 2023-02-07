#!/usr/bin/python3
"""module with a class of Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        """initalizing function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
