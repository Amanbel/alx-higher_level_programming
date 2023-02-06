#!/usr/bin/python3
"""function to print text"""


def text_indentation(text):
    """prints text in a new line after . ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])
