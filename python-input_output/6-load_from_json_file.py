#!/usr/bin/python3
"""Module for loading a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.
    """
    with open("{}".format(filename), 'r', encoding='utf-8') as file:
        object = json.load(file)
        return object
