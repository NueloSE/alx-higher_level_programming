#!/usr/bin/python3
"""
Module title: `0-lookup`

This module contains one function.
"""


def lookup(obj):
    """
    `lookup` function compute avaliable attributes and methods of an object
    Arguments:
            1 object

    Return:
            A list of attributes and methods in obj

    Raises:
            None
    """
    return dir(obj)
