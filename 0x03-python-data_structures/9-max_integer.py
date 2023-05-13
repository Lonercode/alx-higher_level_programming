#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    else:
        max = my_list[0]
        for integer in range(len(my_list)):
            if my_list[integer] > max:
                max = my_list[integer]
        return (max)
