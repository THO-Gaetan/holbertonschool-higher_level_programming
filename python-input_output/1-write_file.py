#!/usr/bin/python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file.
    """
    with open(filename, "w", enconding="utf-8") as file:
        return file.write(text)
