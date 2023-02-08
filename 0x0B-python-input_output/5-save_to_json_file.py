#!/usr/bin/python3
"""module of a function"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes json string to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
