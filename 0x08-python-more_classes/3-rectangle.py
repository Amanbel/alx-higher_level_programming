#!/usr/bin/python3
"""module of a class"""


class Rectangle:
    """class of Rectangle with area and perimeter metthod"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.height == 0 or self.width ==0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ''
        string = ''
        for i in range(self.height):
            for j in range(self.width):
                string += '#'
            if i != self.height - 1:
                string += '\n'
        return string
