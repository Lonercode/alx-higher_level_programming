#!/usr/bin/python3
for l in range(97, 123):
    if l == 112 or l == 101:
        continue
    print(f"{chr(l)}", end = "")
