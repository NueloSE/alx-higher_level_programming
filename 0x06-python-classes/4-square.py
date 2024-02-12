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
        self.__size = size

    @property
    def size(self):
        """
        This is simple a getter function
        it return the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is simple a setter function
        it sets the size attribute
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method helps compute the area of a square

        Formula for area of square:
            square of the sizes
            i.e: size ^ 2
        """
        return (self.__size) ** 2
