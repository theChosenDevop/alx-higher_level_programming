#!/usr/bin/python3
""" defined class MyList inherits super class list """


class MyList(list):
    """
        MyList: Derived class of list

        Args:
            list: Base class
    """

    def print_sorted(self):
        """ print sorted list in ascending order """
        print(sorted(self))
