#!/usr/bin/python3
"""module of a class"""


class Rectangle:
    """rectangle class which has area and perimeter methods"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width:

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def primeter(self):
        """calculates the perimeter of Rectangle"""
        if self.__width == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
