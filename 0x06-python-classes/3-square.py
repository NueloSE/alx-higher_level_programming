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
    def __init__(self, size=0):
        """
        The __init__ method used to initilize the
        private varaiable for an instance
        Args:
            param1(size): the size of the square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This method helps compute the area of a square

        Formula for area of square:
            square of the sizes
            i.e: size ^ 2
        """
        return (self.__size) ** 2
