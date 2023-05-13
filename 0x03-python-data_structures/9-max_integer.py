#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    else:
        max = 0
        for integer in range(0, len(my_list)):
            if my_list[integer] > max:
                max = my_list[integer]
        return (max)
