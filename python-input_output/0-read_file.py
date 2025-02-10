#!/usr/bin/python3


def read_file(filename=""):
    with open("{}".format(filename), enconding="utf-8") as file:
        content = file.read()
        print("{}".format(content), end="")
