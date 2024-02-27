#!/usr/bin/python3
"""Module name: ``rectangle``"""
from models.base import Base


class Rectangle(Base):
    """
    A class that inherits from Base model
    Creates an instance of Rectangle obj with some methods & attr.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """An initializer method"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method"""
        self.__width = value

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        self.__y = value
