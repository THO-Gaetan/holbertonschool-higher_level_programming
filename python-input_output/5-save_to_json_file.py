#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    with open("{}".format(filename), "w", enconding="utf-8") as file:
        result = json.dump(my_obj, file)
        return result
