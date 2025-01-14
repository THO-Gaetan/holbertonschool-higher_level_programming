#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    print('{}'.format(str(number)[-1]), end='')
    return int(number) % 10
