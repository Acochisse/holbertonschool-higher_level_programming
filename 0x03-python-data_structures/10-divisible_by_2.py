#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = list(my_list)
    if my_list is None:
        return None:
    for i in my_list:
        if (i % 2 is 0):
            ret[i] = True
        else:
            ret[i] = False
    return ret
