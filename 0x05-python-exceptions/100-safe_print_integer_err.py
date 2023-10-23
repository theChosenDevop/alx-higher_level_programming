#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
        safe_print_integer_err
            The function prints an integer

        Args:
            value: integer

        Returns:
            True if value has been correctly printed that is
            value is an integer or False if otherwise and prints
            in stderr
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
