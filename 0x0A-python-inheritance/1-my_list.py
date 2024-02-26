#!/usr/bin/python3
"""
Module title: `1-my_list`
This module contains one function.
"""


class MyList(list):
    """
    A class that inherits the list module
    contains some method
    """
    def __init__(self):
        """ initializing objects"""
        super().__init__()

    def print_sorted(self):
        """
        print_sorted:
        """
        print(sorted(self))
