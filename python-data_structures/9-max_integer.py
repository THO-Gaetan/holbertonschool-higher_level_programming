#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    if len(my_list) == 0:
        return None
    for integer in my_list:
        if integer > max_value:
            max_value = integer
    return max_value
