#!/usr/bin/python3
"""" Defines a function that check instance of a class that inherited  """


def inherits_from(obj, a_class):
    """
        obj: object to be compared
        a_class: class type
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
