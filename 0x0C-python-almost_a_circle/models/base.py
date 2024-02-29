#!/usr/bin/python3
"""Model name: ``base``"""
import json


class Base:
    """
    class name: ``Base``
    creates a simple object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """A method which initializes the class properties"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a passed list as a json object"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A method that saves to a file"""
        filename = type(list_objs).__name__ + '.json'
        json_obj = cls.to_json_string(list_objs)
        with open(filename, 'w') as afile:
            json.dump(json_obj, afile)
