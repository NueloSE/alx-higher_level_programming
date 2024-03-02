#!/usr/bin/python3
"""Model name: ``base``"""
import json
import os
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
