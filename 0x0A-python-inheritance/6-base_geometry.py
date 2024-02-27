#!/usr/bin/python3
""" Module name: 6-base_geometry"""


class BaseGeometry(Exception):
    """The class contains an initializer and area method"""
    def __init__(self):
        """An initialize with just a pass"""
        pass

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
