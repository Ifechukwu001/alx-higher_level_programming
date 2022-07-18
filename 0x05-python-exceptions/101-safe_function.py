#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as e:
        sys.stderr.write("Exception: ")
        sys.stderr.write(e.args[0])
        sys.stderr.write("\n")
        return None
