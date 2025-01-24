#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        a = int(a) if isinstance(a, float) else a
        b = int(b) if isinstance(b, float) else b
        return a + b
    except TypeError:
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        if not isinstance(b, int):
            raise TypeError("b must be an integer")
