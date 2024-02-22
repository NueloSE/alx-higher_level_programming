#!/usr/bin/python3
""""
Module name: 6-load_from_json_file

Contains just one function that loads from json file
"""
import json


def load_from_json_file(filename):
    """
    loads a json file.

    Parameters:
    my_string (JSON object): The object to be converted to python obj.

    Returns:
    obj: A python obj.
    """
    with open(filename, "r", encoding='utf-8') as openFile:
        return (json.load(openFile))
