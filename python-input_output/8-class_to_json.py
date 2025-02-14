#!/usr/bin/python3
"""Module for converting a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
