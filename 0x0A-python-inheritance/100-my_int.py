#!/usr/bin/python3
"""class module"""


class MyInt(int):
    """subclass of int"""
    def __eq__(self, value):
        """overrides equal"""
        return int(self) != int(value)

    def __ne__(self, value):
        """overrides not equal"""
        return int(self) == int(value)
