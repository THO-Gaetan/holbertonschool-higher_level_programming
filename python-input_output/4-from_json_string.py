#!/usr/bin/python3
"""Module for converting a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.
    """
    return json.loads(my_str)
