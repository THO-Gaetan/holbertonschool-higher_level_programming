#!/usr/bin/python3
"""Module for converting an object to a JSON string."""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON string representation.
    """
    return json.dumps(my_obj)
