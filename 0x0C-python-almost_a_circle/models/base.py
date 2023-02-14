#!/usr/bin/python3
"""module of a class"""
import json


class Base:
    """a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns serialized json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """classmethod that saves json string to file"""
        dict_list = []
        filename = "{}.json".format(cls.__name__)
        for objs in list_objs:
            d = objs.to_dictionary()
            dict_list.append(d)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(dict_list))
