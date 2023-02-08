#!/usr/bin/python3
"""module of a function"""


def write_file(filename="", text=""):
    """function to write to a file"""
    with open(filename, "w") as f:
        return f.write(text)

