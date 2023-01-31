#!/usr/bin/python3
"""class accepts arguments"""


class Square:
    """class which has a private size attribute"""
    def __init__(self, size=0):
        """initialization function"""
        self.size = size

    @property
    def size(self):
        """property attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """property setter"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """function that calculates the area of the square"""
        return self.__size ** 2
