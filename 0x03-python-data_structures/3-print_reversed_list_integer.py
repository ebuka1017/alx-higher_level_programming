#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_l = reversed(my_list)
    for x in new_l:
        print("{:d}".format(x))
