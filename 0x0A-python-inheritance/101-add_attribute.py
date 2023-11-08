#!/bin/usr/python3
""" Defines function add_attribute """


def add_attribute(obj, attr_name, attr_value):
    """"add attribute to instance of a class
        and throws error if it can't

        Args:
            obj: obj to add attribute to
            attr_name: attribute name
            attr_value: attribute value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
