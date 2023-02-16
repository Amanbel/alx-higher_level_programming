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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """classmethod that saves json string to file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [objs.to_dictionary() for objs in list_objs]
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new updated instance"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(12, 14)
            else:
                dummy = cls(12)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """loads serialized file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename) as f:
            return json.load(f)
