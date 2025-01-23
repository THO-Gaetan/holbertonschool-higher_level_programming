#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b == 0:
            result = None
        else:
            result = a / 2
    except (ValueError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))
        return result