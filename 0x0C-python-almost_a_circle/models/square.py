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
