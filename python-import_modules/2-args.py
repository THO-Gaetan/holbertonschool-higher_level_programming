#!/usr/bin/python3
import sys
if len(sys.argv) - 1 == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(sys.argv) - 1))
for index, args in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(index, args))
