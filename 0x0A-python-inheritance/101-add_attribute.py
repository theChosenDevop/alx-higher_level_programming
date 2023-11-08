#!/usr/bin/python3
""" Defines function add_attribute """


def add_attribute(obj, attr_name, attr_value):
    """
    Args:
            obj: obj to add attribute to
            attr_name: attribute name
            attr_value: attribute value
    Raises:
            TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
