#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
        result = 0
    for char in roman_string:
        if char == "I":
            result += 1
        elif char == "V":
            result += 5
        elif char == "X":
            result += 10
        elif char == "L":
            result += 50
        elif char == "C":
            result += 100
        elif char == "D":
            result += 500
        elif char == "M":
            result += 1000
    return result
    