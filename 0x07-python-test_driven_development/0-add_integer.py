#!/usr/bin/python3
"""This module contains the add_integer function
The add_integer function computes the summation of two integer value
It takes 2 arguments a and b
a and b must be integer
The function doesn't work with string"""


def add_integer(a, b=98):
    """it can work with just one argument and automatically
    set the second as 98
    Returns: a + b
    """
    if not (isinstance(a, int) | isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) | isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(int(a) + int(b))
