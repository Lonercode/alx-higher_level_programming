#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    else:
        sumz = 0
        und = 0
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                allz = my_list[i][j] * (my_list[i][j - 1])
            sumz += allz
            und += my_list[i][1]
        return (float(sumz / und))
