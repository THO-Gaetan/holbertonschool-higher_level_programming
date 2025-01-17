#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for index, args in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(index, args))
