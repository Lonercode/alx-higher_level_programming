#!/usr/bin/python3
def remove_char_at(str, n):
        replace = " "
        str = replace + str[:n] + str[n + 1:]
        print(str)
