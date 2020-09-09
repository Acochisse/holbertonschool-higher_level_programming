#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = my_list.copy()
    for i in my_list:
        if (ret[i] % 2 == 0):
            ret[i] = True
        else:
            ret[i] = False
    return ret
