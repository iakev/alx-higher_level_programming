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
            f"{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter for size
        """

        return getattr(self, 'width')

    @size.setter
    def size(self, val):
        super().validate_height_width("width", val)
        setattr(self, 'width', val)
        setattr(self, 'height', val)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute from args
        """

        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        Returns dictionary representation of Rectangle instances
        """

        attrs = {}
        keys = ['id', 'size', 'x', 'y']
        for key in keys:
            attrs[key] = getattr(self, key)
        return attrs
