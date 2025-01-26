#!/usr/bin/python3
"""Module containing say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Function that print first_name and last_name, only if both are string"""
    # Check first if first_name or last_name are a string or not
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # print the first and last name
    print("My name is {} {}".format(first_name, last_name))
