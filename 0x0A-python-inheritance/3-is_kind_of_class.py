#!/usr/bin/python3
"""Module name: ``3-is_kind_of_class``"""


def is_kind_of_class(obj, a_class):
    """Check if an obj and a class have same kind"""
    return (isinstance(obj, a_class) | issubclass(type(obj), a_class))
