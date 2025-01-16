#!/usr/bin/python3
import sys
print("{} arguments:".format(len(sys.argv) - 1))
for index, args in enumerate(sys.argv[1:], start=1):
    print("{} : {}".format(index, args))
