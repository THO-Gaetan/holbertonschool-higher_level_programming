#!/usr/bin/python3
"""Module containing add_integer function"""


def add_integer(a, b=98):
    """Function to return a + b"""
    # Checking if a and b are float to turn into int
    try:
        a = int(a) if isinstance(a, float) else a
        b = int(b) if isinstance(b, float) else b
        return a + b
    except TypeError:
        # if float are neither an int or a float raise a TypeError
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        if not isinstance(b, int):
            raise TypeError("b must be an integer")
