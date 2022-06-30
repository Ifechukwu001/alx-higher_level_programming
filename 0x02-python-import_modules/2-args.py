#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    suffix = "arguments"
    endl = ":"
    if argc == 1:
        endl = "."
    elif argc == 2:
        suffix = "argument"

    if argc == 1:
        print("0 {}{}".format(suffix, endl))
    else:
        print("{:d} {}{}".format(argc - 1, suffix, endl))
        for i in range(1, argc):
            print("{:d}: {}".format(i, argv[i]))
