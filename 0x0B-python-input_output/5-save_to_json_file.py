#!/usr/bin/python3
""""
Module name: 5-save_to_json_file.py

Contains just one function that saves json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Converts the given JSON to a python obj.

    Parameters:
    my_string (JSON object): The object to be converted to python obj.

    Returns:
    obj: A python obj.
    """
    with open(filename, "w", encoding="utf-8") as openFile:
        json_obj = json.dump(my_obj, openFile)
