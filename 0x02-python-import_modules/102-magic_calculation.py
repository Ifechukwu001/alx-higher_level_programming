#!/usr/bin/python3
def magic_calculation(a, b):
    import magic_calculation_102
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)