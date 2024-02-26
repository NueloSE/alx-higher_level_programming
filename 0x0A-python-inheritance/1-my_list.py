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
    def print_sorted(self):
        """
        print_sorted:
            arrange a list in a sorted form
        Arguments:
            1 unsorted iterable like a list

        Return:
            A sorted iterable

        Raises:
            None
        """
        sorted_matrix = sorted(self)
        print(sorted_matrix)
        return sorted_matrix
