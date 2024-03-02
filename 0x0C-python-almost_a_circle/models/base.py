#!/usr/bin/python3
"""Model name: ``base``"""
import json
import os
import csv


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
        """Saves to a csv file"""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if list_objs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.width,
                                        obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size,
                                        obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads obj from a csv"""
        filename = cls.__name__ + '.csv'
        instances = []
        if not os.path.exists(filename):
            return instances
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    instance = cls.create(id=int(row[0]), width=int(row[1]),
                                          height=int(row[2]), x=int(row[3]),
                                          y=int(row[4]))
                elif cls.__name__ == "Square":
                    instance = cls.create(id=int(row[0]), size=int(row[1]),
                                          x=int(row[2]), y=int(row[3]))
                instances.append(instance)
        return instances
