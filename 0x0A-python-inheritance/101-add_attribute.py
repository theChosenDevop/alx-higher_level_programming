#!/bin/usr/python3
""" Defines function add_attribute """


def add_attribute(obj, attr_name, attr_value):
    """"add attribute to instance of a class
        and throws error if it can't
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
