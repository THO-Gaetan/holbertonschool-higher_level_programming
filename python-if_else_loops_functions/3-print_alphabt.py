#!/usr/bin/python3
for i in range(97, 123):
    asc = chr(i)
    if asc != 'q' and asc != 'e':
        print(f"{asc}", end="")
