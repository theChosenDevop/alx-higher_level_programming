#!/usr/bin/python3
""" Defines empty class """


class BaseGeometry:
    """ implements area function """
    def area(self):
        """" raise exception message """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
            self: object representation
            value: input
            name: input
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
