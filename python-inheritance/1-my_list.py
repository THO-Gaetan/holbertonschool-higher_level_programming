#!/usr/bin/python3
"""create the class MyList"""


class MyList(list):
    """initialise the list attribute"""
    def __init__(self, iterable=None):
        super().__init__(iterable or [])

    def print_sorted(self):
        print(sorted(self))
