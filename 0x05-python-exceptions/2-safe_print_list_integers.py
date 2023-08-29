#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    if(my_list):
        for i in range(x):
            if isinstance(my_list[i], int):
                try:
                    print("{:d}".format(my_list[i]), end='')
                    count += 1
                except (ValueError, IndexError):
                    print()
    print()
    return count
