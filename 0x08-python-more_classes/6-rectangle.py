#!/usr/bin/python3
"""module of a class"""


class Rectangle:
    """class of rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        string = ''
        for i in range(self.height):
            for j in range(self.width):
                string += '#'
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
