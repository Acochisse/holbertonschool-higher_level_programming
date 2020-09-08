#!/usr/bin/python3
def no_c(my_string):
    stralt = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            stralt += i
    return stralt
