#!/usr/bin/python3
"""create a class named Square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """The square class that define the area of a square"""
    def __init__(self, size):
        """initialise the size of the square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[square] {}/{}".format(self.__size, self.__size)
