#!/usr/bin/python3
"""Model name: ``base``"""
import json
import os


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
        """A method that saves class attribute in json format to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as afile:
            if list_objs is None:
                afile.write('[]')
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                afile.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """A static method that load a json string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A method that returns an instance with all attribute alreaady set"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """A method that loads from a file"""
        filename = cls.__name__ + '.json'
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, 'r') as afile:
                json_str = afile.read()
                json_dic = cls.from_json_string(json_str)
                instances = []
                for jdict in (json_dic):
                    instance = cls.create(**jdict)
                    instances.append(instance)
                return instances
