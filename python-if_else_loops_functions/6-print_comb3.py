#!/usr/bin/python3
i = 0
while i <= 8:
    n = i + 1
    while n <= 9:
        if i == 8 and n == 9:
            print("{}{}".format(i, n))
        else:
            print("{}{}".format(i, n), end=", ")
        n += 1
    i += 1
