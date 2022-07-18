#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Safely prints only integers in a list """
    elem_no = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            elem_no += 1
        except (ValueError, TypeError):
            continue;
    print()
    return elem_no
