#!/usr/bin/python3
"""
This module prints a square with the character #

Example:
    print_square(2)
Output:
    ##
    ##
"""


def print_square(size):
    """
    print size number of # to the stdout in form of a square
    Argument:
        size: the size of the square
    Raise:
        TypeError: if size is not an integer
        ValueError: if size is less 0
        TypeError: size a float and less than 0
    """
    if not (isinstance(size, int)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if (isinstance(size, float)) and (size < 0):
        raise TypeError('size must be an integer')
    size = int(size)
    i = size
    while (i > 0):
        j = 0
        while (j < size):
            print("#", end='')
            j += 1
        i -= 1
        print()
