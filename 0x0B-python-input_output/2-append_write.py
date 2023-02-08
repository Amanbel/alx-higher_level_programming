#!/usr/bin/python3
"""module for function"""


def append_write(filename="", text=""):
    """function that appends string to the file"""
    with open(filename, "a") as f:
        return f.write(text)
