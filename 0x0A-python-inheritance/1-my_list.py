#!/usr/bin/python3
"""module with class that inherites from list"""

class MyList(list):
    """subclass of list"""


    def print_sorted(self):
        print(sorted(self))
