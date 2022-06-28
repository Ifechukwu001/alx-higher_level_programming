#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print(f"{i:d}{j:d}", end="")
        if i == 8:
            print("")
        else:
            print(", ", end="")
