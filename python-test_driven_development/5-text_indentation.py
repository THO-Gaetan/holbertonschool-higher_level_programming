#!/usr/bin/python3
"""Module containing text_indentation function"""


def text_indentation(text):
    """Function to print a text with a new line when specific encouter"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation = {'.', '?', ':'}
    new_line = 0
    for i, char in enumerate(text):
        if char in punctuation:
            print(text[new_line: i + 1].strip() + "\n")
            new_line = i + 1
    if new_line < len(text):
        print(text[new_line:].strip(), end="")
