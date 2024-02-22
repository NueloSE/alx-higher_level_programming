#!/usr/bin/python3
"""
Module: json_serializer

This module provides a function for serializing
the attributes of an object into a dictionary suitable for JSON serialization.

Functions:
    - class_to_json(obj): Serialize the attributes of
    an object into a dictionary suitable for JSON serialization.

Usage:
    from json_serializer import class_to_json
    obj = MyClass()
    serialized_data = class_to_json(obj)
"""


def class_to_json(obj):
    """
    Serialize the attributes of an object into
    a dictionary suitable for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are serializable.

    Returns:
        dict: A dictionary containing the serialized attributes of the object.

    Raises:
        TypeError: If the object is not an instance of a class.
    """
    attributes = obj.__dict__

    serialized = {
        key: value for key, value in attributes.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

    return serialized
