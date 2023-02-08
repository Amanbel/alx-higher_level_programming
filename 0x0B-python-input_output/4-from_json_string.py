#!/usr/bin/python3
"""module for a function"""
import json


def from_json_string(my_str):
    """function that returns the object form of my_str"""
    string = json.loads(my_str)
    return string
