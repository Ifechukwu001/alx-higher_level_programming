#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string
    while True:
        if "c" in new_string:
            idx = new_string.index("c")
            new_string = new_string[:idx] + new_string[idx + 1:]
        elif "C" in new_string:
            idx = new_string.index("C")
            new_string = new_string[:idx] + new_string[idx + 1:]
        else:
            break
    return new_string
