#!/usr/bin/python3
"""module of a class"""
from .base import Base


class Rectangle(Base):
    """a subclass of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """x getter function"""
        return self.__x

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @width.setter
    def width(self, width):
        """width setter function"""
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """height setter function"""
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """x setter function"""
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """y setter function"""
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """funciton to calculate area of rectangle"""
        return self.height * self.width

    def display(self):
        """function to display the rectangle with # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print('#', end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """returns readable string"""
        return "[Rectangle] ({}) {}/{}\
 -\
 {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """updates class attributes"""
        varlist = [super().__init__, self.width, self.height, self.x, self.y]
        for i in range(len(args)):
            varlist[i] = args[i]
