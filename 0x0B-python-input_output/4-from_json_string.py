#!/usr/bin/python3
""""
Module name: 4-from_json_string

contains one function that converts json obj to python obj
"""
import json


def from_json_string(my_string):
    """
    Converts the given JSON to a python obj.

    Parameters:
    my_string (JSON object): The object to be converted to python obj.

    Returns:
    obj: A python obj.
    """
    return (json.loads(my_string))
