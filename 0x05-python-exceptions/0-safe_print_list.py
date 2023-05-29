#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for intg in range(x):
        try:
            print("{}".format(my_list[intg]), end="")
            num += num
        except IndexError:
            continue
    print("")
    return num
