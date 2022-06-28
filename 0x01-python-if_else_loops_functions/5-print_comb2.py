#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        print("{:d}{:d}".format(i, j), end="")
        if i == 9 and j == 9:
            end_char = "\n"
        else:
            end_char = ", "
        print(end_char, end="")
