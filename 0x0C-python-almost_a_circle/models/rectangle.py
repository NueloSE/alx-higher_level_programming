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

        self._is_int({'width': width, 'height': height, 'x': x, 'y': y})
        self._greater_than_zero({'width': width, 'height': height})
        self._less_than_zero({'x': x, 'y': y})

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def to_dictionary(self):
        """Returns a dictionary of class attributes"""
        new_dic = {
            'x': self.x, 'y': self.y, 'id': self.id,
            'height': self.height, 'width': self.width,
        }
        return new_dic

    def update(self, *args, **kwargs):
        """Enable attributes of and instance to be updated"""
        if len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __str__(self):
        """Allows for printing format str to stdout"""
        return (
            f"[{type(self).__name__}] ({self.id}) "
            f"{self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def display(self):
        """Prints in stdout the Rectangle with the character #"""
        for yl in range(self.__y):
            print()
        for i in range(self.__height):
            for xl in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def area(self):
        """Returns width * height i.e area of the rectangle"""
        return self.__width * self.__height

    @staticmethod
    def _is_int(kwargv):
        """A validator to ensure only integer values is passed"""
        for key, value in kwargv.items():
            if not isinstance(value, int):
                raise TypeError(f"{key} must be an integer")

    @staticmethod
    def _greater_than_zero(kwargv):
        """A validator to ensure that width and height is a positive int"""
        for key, value in kwargv.items():
            if value <= 0:
                raise ValueError(f"{key} must be > 0")

    @staticmethod
    def _less_than_zero(kwargv):
        """A validator to ensure x and y is not negative"""
        for key, value in kwargv.items():
            if value < 0:
                raise ValueError(f'{key} must be >= 0')

    @property
    def width(self):
        """Width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method"""
        self._is_int({'width': value})
        self._greater_than_zero({'width': value})
        self._less_than_zero({'width': value})
        self.__width = value

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""
        self._is_int({'height': value})
        self._greater_than_zero({'height': value})
        self._less_than_zero({'height': value})
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        self._is_int({'x': value})
        self._greater_than_zero({'x': value})
        self._less_than_zero({'x': value})
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        self._is_int({'y': value})
        self._greater_than_zero({'y': value})
        self._less_than_zero({'y': value})
        self.__y = value
