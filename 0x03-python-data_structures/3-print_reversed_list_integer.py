#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list1 = my_list[::-1]
        for integer in my_list1:
            print("{:d}".format(integer))
