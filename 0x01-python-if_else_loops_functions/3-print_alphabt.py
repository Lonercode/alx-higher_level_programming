#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet == 112 or alphabet == 101:
        continue
    print("{}".format(chr(alphabet)), end="")
