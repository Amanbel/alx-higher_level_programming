#!/usr/bin/python3
"""module of a function"""


def write_file(filename="", text=""):
    """function to write to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        file = f.write(text)
        string = file.read()
        return len(string)

