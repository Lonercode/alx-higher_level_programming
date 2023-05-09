#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if chr(i) == c and i>=97 and i<=122:
            return (True)
        else:
            return (False)
