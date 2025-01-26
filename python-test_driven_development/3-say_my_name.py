#!/usr/bin/python3
"""Module containing say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Function that print first_name and last_name, only if both are string"""
    err_msg = "first_name must be a string or last_name must be a string"
    # Check first if first_name or last_name are a string or not
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(err_msg)
    # print the first and last name
    print("{} {}".format(first_name, last_name))
