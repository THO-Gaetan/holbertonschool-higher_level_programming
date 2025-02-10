#!/usr/bin/python3

import json


def load_from_json_file(filename):
    with open("{}".format(filename)) as file:
        object = json.load(file)
        return object