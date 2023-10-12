#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    total = 0
    unique_elem = set()
    for num in my_list:
        if num not in unique_elem:
            total += num
            unique_elem.add(num)
    return total
