#!/usr/bin/python3
def print_last_digit(number):
    l_digit = abs(number - (int(number / 10) * 10))
    print(f"{l_digit:d}", end="")
    return l_digit
