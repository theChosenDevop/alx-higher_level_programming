#!/usr/bin/python3

def safe_print_integer(value):
    """
        safe_print_integer
             prints an integer with "{:d}".format()

        Args:
            value: integer

        Return:
            True if value is correctly printed or False if otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
