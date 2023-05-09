#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) in range(97, 123):
            letter = chr(ord(i) - 32)
        print("{}".format(letter), end="")
    print("")

