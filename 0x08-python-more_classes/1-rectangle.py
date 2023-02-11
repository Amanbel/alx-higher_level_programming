#!/usr/bin/python3
"""module for a class"""


class Rectangle:
    """class with getters and setters"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """getter of height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
