#!/usr/bin/python3
"""creating a BaseGeometry class"""


class BaseGeometry:
    """setting up the BaseGeometry with area def"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
