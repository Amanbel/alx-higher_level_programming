#!/usr/bin/python3
"""module for a function"""


def read_file(filename=""):
    """reads from file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        string = f.read()
        print(string, end="")
