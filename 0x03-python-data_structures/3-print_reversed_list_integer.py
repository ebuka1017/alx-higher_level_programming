#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_l = my_list
    my_list.reverse()
    for x in new_l:
        print("{:d}".format(x))
