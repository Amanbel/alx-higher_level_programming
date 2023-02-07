#!/usr/bin/python3
"""class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the area of a square"""
        return (self.__size * self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
