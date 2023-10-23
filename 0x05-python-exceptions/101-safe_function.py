#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
        safe_function
            excecutes a function safely

        Args:
            fct: function
            args: arguments

        Return:
            the result of the function
    """
    try:
        product = fct(*args)
    except (ZeroDivisionError, IndexError):
        product = None
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return product
