#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_c = 0
    try:
        for i in range (x):
            print("{}".format(my_list[i], end='')
            print_c += 1

        except IndexError:
            pass

    print()
    return print_C
