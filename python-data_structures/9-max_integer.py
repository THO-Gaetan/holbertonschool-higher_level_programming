#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = 0
    if not my_list:
        return None
    for integer in my_list:
        if integer > max_value:
            max_value = integer
    return max_value
