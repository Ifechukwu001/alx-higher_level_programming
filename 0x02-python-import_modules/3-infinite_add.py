#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    sum = 0
    for index in range(1, argc):
        sum += int(argv[index])
    print("{:d}".format(sum))
