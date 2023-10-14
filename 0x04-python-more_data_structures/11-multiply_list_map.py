#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ multiply list map function

        Args:
            my_list: list of integers
            number: integer

        Returns:
                 a list with all values multiplied by a
                 number without using any loop
    """
    return list(map(lambda x: x * number, my_list))
