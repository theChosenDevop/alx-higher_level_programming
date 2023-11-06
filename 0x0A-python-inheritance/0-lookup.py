#!/usr/bin/python3

def lookup(obj):
    """
        lookup - returns the list of availbale attributes
                 and method of an object

        Args:
            obj: instance of a class
    """
    return dir(obj)
