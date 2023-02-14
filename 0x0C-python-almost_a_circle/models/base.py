#!/usr/bin/python3
"""module of a class"""
import json


class Base:
    """a base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id == None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        elif id != None:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
