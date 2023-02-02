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
        if (type(position[0]) != int && position < 0) && (type(position[1]) != int && position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position


    def area(self):
        """function that calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for m in range(0, self.__position[0]):
                print(" ", end="")

            for j in range(0, self.__size):
                print("#", end="")
            print()
