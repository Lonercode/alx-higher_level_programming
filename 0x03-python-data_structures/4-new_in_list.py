#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        my_list1 = []
        for i in my_list:
            my_list1.append(i)
        my_list1[idx] = element
        return (my_list1)
