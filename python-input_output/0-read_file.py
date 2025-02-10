#!/usr/bin/python3


def read_file(filename=""):
    with open("{}".format(filename)) as file:
        content = file.read()
        print("{}".format(content), end="")
