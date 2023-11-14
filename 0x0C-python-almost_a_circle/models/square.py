#!/usr/bin/python3
""" Defines Derived class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an instance of a Square

        Args:
            size(int): The size of the new Square
            x(int): The x coordinate of the new Square
            y(int): The y coordinate of the new Square
            id(int): The identity of the new Square
        Raises:
                TypeError: if size is not an integer
                ValueError:if size is <= 0
        """
        super().__init__(size, size, x, y, id)
        self.size = size
        
    def __str__(self):
            """ returns string representation """
            return ("[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )
                )
    @property
    def size(self):
            """ Get the size of Square """
            return self.width

    @size.setter
    def size(self, value):
        """ assigns value to attributes """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width mus be > 0")
        self.width = value
        self.height = value
