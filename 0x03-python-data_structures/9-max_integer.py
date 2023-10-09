#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """max integer function

    Args:
        my_list: empty list to receive user input

    Return:
        max integer
    """
    if len(my_list) == 0:
        return None
    max_int = my_list[0]

    for i in range(0, len(my_list)):
        if max_int > my_list[i]:
            max_int = max_int
        else:
            max_int = my_list[i]
    return max_int

"""
    for num in my_list:
        if num > max_int:
            max_int = num

    return max_int
"""
