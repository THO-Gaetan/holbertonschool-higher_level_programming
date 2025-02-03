#!/usr/bin/python3
"""define an object lookup function"""


def lookup(obj):
    """return the list of attributes and methods from an object"""
    return dir(obj)
