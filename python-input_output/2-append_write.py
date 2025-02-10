#!/usr/bin/python3

def append_write(filename="", text=""):
    with open("{}".format(filename), "a") as file:
        return file.write("{}".format(text))
