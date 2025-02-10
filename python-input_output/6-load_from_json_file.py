#!/usr/bin/python3

import json


def load_from_json_file(filename):
    with open("{}".format(filename), 'r', encoding='utf-8') as file:
        object = json.load(file)
        return object
