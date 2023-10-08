#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """My new list
    Args:
        my_list: list of integers
        idx: index of list to be inserted
        element: new element to be inserted in the list

    Return:
        copy of new list
    """
    new_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return new_list
    for i in range(len(new_list)):
        if idx == i:
            new_list[i] = element
    return new_list
