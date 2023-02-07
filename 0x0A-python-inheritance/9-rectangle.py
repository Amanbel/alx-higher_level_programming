#!/usr/bin/python3
"""class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of basegeometry"""
    def __init__(self, width, height):
        """init function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns readable string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
