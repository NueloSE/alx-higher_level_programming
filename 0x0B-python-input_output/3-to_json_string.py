#!/usr/bin/python3
""""
Module name: 3-to_json_string

contains one function that converts python obj to json
"""
import json


def to_json_string(my_obj):
    """
    Converts the given object to its JSON representation as a string.

    Parameters:
    my_obj (object): The object to be converted to JSON.

    Returns:
    str: A string containing the JSON representation of the input object.
    """
    json_obj = (json.dumps(my_obj))
    return json_obj
