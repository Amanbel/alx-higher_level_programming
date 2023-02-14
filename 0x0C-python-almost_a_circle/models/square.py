#!/usr/bin/python3
"""a module for a subclass"""
from .rectangle import Rectangle


class Square(Rectangle):
    """a subclass of rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def area(self):
        """calculates area of square"""
        return self.width * self.height

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, size):
        _size = size
        super(Square, type(self)).width.fset(self, _size)
        super(Square, type(self)).height.fset(self, _size)

    def display(self):
        """function to display the square with # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print('#', end="") for w in range(self.width)]
            print("")

    def __str__(self):
        return '[Square] ({}) {}/{}\
 - {}'.format(self.id, self.x, self.y, self.width)
