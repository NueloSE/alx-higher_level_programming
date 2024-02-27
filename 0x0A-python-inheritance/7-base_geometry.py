#!/usr/bin/python3
""" Module name: 6-base_geometry"""


class BaseGeometry():
    """The class contains an initializer and area method"""
    def __init__(self):
        """An initialize with just a pass"""
        pass

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value passed"""
        if not (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
