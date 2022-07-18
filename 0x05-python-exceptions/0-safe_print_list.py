#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Prints the elements in a list """
    elem_no = 0
    for idx in range(0, x):
        try:
            elem = my_list[idx]
        except IndexError:
            break;
        else:
            elem_no += 1
            print(elem, end="")
    print()
    return elem_no
