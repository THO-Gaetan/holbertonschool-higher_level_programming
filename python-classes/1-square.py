#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size  # Private instance attribute

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.__size

    def get_size(self):
        """Return the size of the square."""
        return self.__size
