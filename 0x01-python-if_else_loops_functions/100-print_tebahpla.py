#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        j = 32
    else:
        j = 0
    print("{}".format(chr(i - j)), end="")
