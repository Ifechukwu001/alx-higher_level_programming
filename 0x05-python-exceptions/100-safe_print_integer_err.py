#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """ Prints integer """
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        sys.stderr.write("Exception: ")
        sys.stderr.write(ve.args[0])
        sys.stderr.write("\n")
        return False
