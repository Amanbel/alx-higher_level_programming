#!/usr/bin/python3
"""class accepts arguments"""


class Square:
    """class which has a private size attribute"""
    def __init__(self, size=0):
        """initialization function"""
        self.size = size
    @size.setter
    def size(self, size):
        """property setter"""
        if isinstance(size, str):
            raise TypeError('size must be an integer')
        else if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
