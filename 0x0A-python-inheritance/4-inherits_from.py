#!/usr/bin/python3
"""Module contains one function"""


def inherits_from(obj, a_class):
    """checks if obj inherits class"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
