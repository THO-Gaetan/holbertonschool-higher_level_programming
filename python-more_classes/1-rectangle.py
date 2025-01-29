#!/usr/bin/python3
"""Module containing Rectangle classe"""


class Rectangle:
    """a class for a Rectangle*"""
    def __init__(self, width=0, height=0):
        """ initialisation of self.width and self.height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width size"""
        return self.__width

    @property
    def height(self):
        """get the height size"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the width size as value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the height size as value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
