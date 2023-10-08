#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """My print reversed list integer function
    Args:
        my_list: empty list

    Returns:
        The reversed integers on a new line
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))
