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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        This method helps to initialize the variables of the instance
        @width: the width of the rectangle
        @height: indicates the hieght of the rectangle
        """
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

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
        @value: width value
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
        it sets the value of height
        @value: the new value of the height
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
        return (2 * (self.__width + self.__height))

    def __str__(self):
        res = ""
        if (self.__width == 0) | (self.__height == 0):
            return res
        self.print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            for j in range(self.__width):
                res += self.print_symbol
            if i + 1 == self.__height:
                res += ""
            else:
                res += "\n"
        return res

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        self.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area()) >= (rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        newRectangle = cls(size, size)
        return newRectangle
