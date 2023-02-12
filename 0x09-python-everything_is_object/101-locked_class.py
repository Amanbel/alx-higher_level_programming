#!/usr/bin/python3
"""module for a class"""
class LockedClass:
    """a class that is allowed to have only one attribute"""
    def __setattr__(self, key, value):
        """a function which filters the attributes"""
        if key == 'first_name':
            self.__dict__[key] = str(value)
        else:
            raise AttributeError('\'LockedClass\' object has no attribute \'last_name\'')
