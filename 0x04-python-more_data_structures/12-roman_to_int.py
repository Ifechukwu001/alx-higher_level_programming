#!/usr/bin/python3
def roman_to_int(roman_string):
    r_numerals = ["I", "V", "X", "L", "C", "D", "M"]
    g_numerals = [1, 5, 10, 50, 100, 500, 1000]
    g_num = 0

    if not isinstance(roman_string, str):
        return 0

    r_num = roman_string.upper()
    for i in r_num:
        num = g_numerals[r_numerals.index(i)]
        if num > g_num:
            g_num = num - g_num
        elif g_num > num:
            g_num += num
    return g_num
