#!/usr/bin/python3
""" Defines MyInt class """


class MyInt(int):
    """ MyInt has == and != operators """
    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
