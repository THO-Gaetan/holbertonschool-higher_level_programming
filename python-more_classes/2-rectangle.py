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

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
