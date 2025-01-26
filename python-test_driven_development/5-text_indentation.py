#!/usr/bin/python3
"""Module containing text_indentation function"""


def text_indentation(text):
    """Function to print a text with a new line when specific encouter"""
    new_line = 0
    # check if text is a string or not
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for string in text:
        # if string is a ".", "?" or ":" we print it and go to the next line
        if string == "." or string == "?" or string == ":":
            new_line = 1
            print("{}".format(string))
        else:
            # if we just got to the next line, we jump another line and
            # don't count the next string
            if new_line == 1:
                print()
                new_line = 0
            else:
                print("{}".format(string), end="")
