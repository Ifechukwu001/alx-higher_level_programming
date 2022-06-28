#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        char = chr(122 - i)
    else:
        char = chr(90 - i)
    print("{}".format(char), end="")
