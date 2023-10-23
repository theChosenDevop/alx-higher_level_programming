#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    safe_print_list
        prints lements in my_list

    Args:
        my_list: list of integers
        x: element of my_list

    Return: counts of element printed
    """
    count = 0

    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
