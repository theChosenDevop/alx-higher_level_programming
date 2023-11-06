#!/usr/bin/python3
""" Defines function to check if class is instance of type class """


def is_same_class(obj, a_class):
    """"
        obj: object to check class
        a_class: class type
    """
    return type(obj) == a_class
