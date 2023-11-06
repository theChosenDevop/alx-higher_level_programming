#!/usr/bin/python3
""" Defines function that checks the class of object """


def is_kind_of_class(obj, a_class):
    """
        obj: Object to be compared
        a_class: class to be checked with
    """
    return isinstance(obj, a_class)
