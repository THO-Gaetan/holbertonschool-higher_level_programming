#!/usr/bin/python3
"""define an objectif inherits_from function"""


def inherits_from(obj, a_class):
    """True if the object is an instance of a sub class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
