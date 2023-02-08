#!/usr/bin/python3
"""module of a function"""
import json


def load_from_json_file(filename):
    """function opens json filename and deserializes it"""
    with open(filename, 'w', encoding='utf-8') as f:
        obj = json.load(f)
        return obj
