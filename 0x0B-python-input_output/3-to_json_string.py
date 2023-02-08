#!/usr/bin/python3
"""module for a function"""
import json


def to_json_string(my_obj):
    """return a json representation string for my_obj"""
    string = json.dumps(my_obj)
