#!/usr/bin/python3
"""Module for saving a Python object to a file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a file as a JSON string.
    """
    with open("{}".format(filename), 'w', encoding='utf-8') as file:
        result = json.dump(my_obj, file)
        return result
