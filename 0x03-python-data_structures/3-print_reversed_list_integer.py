#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last = len(my_list) - 1
    for i in range(last, 0, -1):
        print("{:d}".format(my_list[last]))
