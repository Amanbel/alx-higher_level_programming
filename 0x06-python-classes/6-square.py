#!/usr/bin/python3
"""class accepts arguments"""


class Square:
    """class which has a private size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization function"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property attribute"""
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        """property setter"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for item in position:
            if type(item) != int or item < 0:
                raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """function that calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        n = self.__position[1]
        w = self.__position[0]
        if self.__size == 0:
            print()
        for nl in range(n):
            print()
        for R in range(self.__size):
            print((' ' * w) + ('#' * self.__size))
