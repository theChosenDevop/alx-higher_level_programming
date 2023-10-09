#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """no c function
        Args:
            my_string

        Return:
            new string
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
