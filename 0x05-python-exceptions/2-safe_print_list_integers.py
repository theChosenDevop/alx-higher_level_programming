#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
        safe_print_list_integers
            prints the first x elements of a list

        Args:
            my_list: list
            x: element of the list

        Return:
            real number of integers printed
    """
    count = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
