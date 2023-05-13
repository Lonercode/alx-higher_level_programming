#!/usr/bin/python3
if __name__ == "__main__":
    def print_reversed_list_integer(my_list=[]):
        my_list1 = my_list[::-1]
        for integer in my_list1:
            print("{}".format(integer))
