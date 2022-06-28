#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr((ord(char) - ord("a")) + ord("A"))
        print(char, end="")
    print("")
