#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    val = sum(i[0] * i[1] for i in my_list)
    av = sum(j[1] for j in my_list)
    return (val / av)
