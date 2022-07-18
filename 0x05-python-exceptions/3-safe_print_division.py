#!/usr/bin/python3
def safe_print_division(a, b):
    """ Prints the division of two numbers safely """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return result
    finally:
        print("Inside result: {}".format(result))
    return result
