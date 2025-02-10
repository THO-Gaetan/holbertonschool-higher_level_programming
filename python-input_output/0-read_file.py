#!/usr/bin/python3
"""
This module contains a function to read and print the contents
of a UTF-8 text file.
"""


def read_file(filename=""):
    """
    the function that read the given file
    """
    with open(filename, "r", enconding='utf-8') as file:
        content = file.read()
        print(content, end="")
