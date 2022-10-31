#!/usr/bin/python3
"""
Module that defines a square class that inherits
from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class ingeriting from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initailizing function
        """

        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """
        String representaion for Square class
        """

        return f"[Square] ({self.id}) " \
            f"{self.x}/{self.y} - {self.width}/{self.height}"
