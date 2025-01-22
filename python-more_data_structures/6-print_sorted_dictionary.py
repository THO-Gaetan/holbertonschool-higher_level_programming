#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dir = sorted(a_dictionary.items())
    for key, value in sorted_dir:
        print('{}: {}'.format(key, value))