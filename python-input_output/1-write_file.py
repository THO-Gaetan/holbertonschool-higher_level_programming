#!/usr/bin/python3

def write_file(filename="", text=""):
    with open("{}".format(filename), "w") as file:
        return file.write("{}".format(text))
