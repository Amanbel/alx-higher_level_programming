#!/usr/bin/python3
"""class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of rectangle"""
    def __init__(self, size):
        self.integer_validator("width", size)
        self.integer_validator("height", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates the area of a square"""
        return super().area()

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
