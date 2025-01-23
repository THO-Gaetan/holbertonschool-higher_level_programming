#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for value in new_dict:
        new_dict[value] = new_dict[value] * 2
    return new_dict
