#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if my_list == "":
        return None
    else:
        max_int = 0
        for i in range(0, len(my_list)):
            if max_int > my_list[i]:
                max_int = max_int
            else:
                max_int = my_list[i]
        return max_int
