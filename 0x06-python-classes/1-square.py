#!/usr/bin/python3

"""
This module help the learner understand OOP

This module has a class Square

Discription of the Square class can be found in the Square class def
"""


class Square():
    """
    This class is an empty class
    The only function carried out by this class
    Is creates an instance of the class without
    any attribute or method.
    """
    def __init__(self, size):
        """
        The __init__ method used to initilize the
        private varaiable for an instance
        Args:
            param1(size): the size of the square
        """
        self.__size = size
