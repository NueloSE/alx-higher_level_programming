#!/usr/bin/python3
"""
This module is a Rectangle module

it will carryout various operations on a triangle

triangle of different size and propertes
"""


class Rectangle:
    """
    This class is all about an object of rectangle type

    it performs several operations on a triangle
    """
    def __init__(self, width=0, height=0):
        """
        This method helps to initialize the variables of the instance
        @width: the width of the rectangle
        @height: indicates the hieght of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This method has been decorated to be a getter
        it gets the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method is decorated as a setter
        it sets the value of width
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        This method has been decorated to be a getter
        it gets the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method is decorated as a setter
        it sets the value of width
        """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        This is a method for calculating the area of a rectangle
        The formular for area of a rectangle is:
                Area = Width * Height
        Return the computed area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        This is a method for calculating the perimeter of a rectangle
        The formular for perimeter of a rectangle is:
                perimeter = 2 * (width + height)
        If width or height is equal to 0, perimeter is equal to 0
        Return the computed perimeter
        """
        if (self.__width == 0) | (self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))
