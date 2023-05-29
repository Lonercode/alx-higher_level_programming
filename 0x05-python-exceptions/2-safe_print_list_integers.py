#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for intg in range(x):
        try:
            print("{:d}".format(my_list[intg]), end="")
            num += num
        except (TypeError, ValueError):
            pass
    print("")
    return num
