#!/usr/bin/python3
"""Module name: ``square``"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class name: ``Square``
    Inherits: Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """An initializer"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A magic method"""
        return (
            f"[{type(self).__name__}] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}"
        )

    @property
    def size(self):
        """A getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """A setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the value of size"""
        if len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Returns a dictionary of class attributes"""
        new_dic = {
            'id': self.id, 'x': self.x,
            'size': self.size, 'y': self.y,
        }
        return new_dic
