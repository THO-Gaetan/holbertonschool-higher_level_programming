#!/usr/bin/python3
"""Module containing Square classe"""


class Square:
    """a class for a Square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
