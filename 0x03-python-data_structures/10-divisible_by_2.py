#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """ divisible by 2 function

    Args:
        my_list: list of user input

    Return:
        True if divisible by 2 or False if otherwise
    """
    bool_val = []
    for i in my_list:
        if i % 2 == 0:
            bool_val.append(True)
        else:
            bool_val.append(False)
    return bool_val
