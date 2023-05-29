#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    intg = 0
    other_list = []
    for intg in range(list_length):
        try:
            i = my_list_1[intg] / my_list_2[intg]
        except TypeError:
            print("wrong type")
            i = 0
        except ZeroDivisionError:
            print("division by 0")
            i = 0
        except IndexError:
            print("out of range")
            i = 0
        finally:
            other_list.append(i)
    return other_list
