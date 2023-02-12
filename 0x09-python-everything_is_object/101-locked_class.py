#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, key, value):
        if key == 'first_name':
            self.__dict__[key] = str(value)
        else:
            raise AttributeError('\'LockedClass\' object has no attribute \'last_name\'')
