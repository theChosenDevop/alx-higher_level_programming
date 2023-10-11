#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """My print reversed list integer function
    Args:
        my_list: empty list

    Returns:
        None
    """
    if not my_list:
        return
    print(my_list[-1])
    print_reversed_list_integer(my_list[:-1])
