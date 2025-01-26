#!/usr/bin/python3
"""Module containing text_indentation function"""


def text_indentation(text):
    """Function to print a text with a new line when specific encouter"""
    new_line = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for string in text:
        if string == "." or string == "?" or string == ":":
            new_line = 1
            print("{}".format(string))
        else:
            if new_line == 1:
                print()
                new_line = 0
            else:
                print("{}".format(string), end="")
