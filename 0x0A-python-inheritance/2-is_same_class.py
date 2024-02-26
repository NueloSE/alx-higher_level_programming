#!/usr/bin/python3
""" module name:
        ``2-is_same-class``
    It contains a simple function
"""


def is_same_class(obj, a_class):
    """
    Check if obj equal a_class
    Return: True on success
    Otherwise: False
    """
    if ((type(obj) is a_class)):
        return True
    return False
