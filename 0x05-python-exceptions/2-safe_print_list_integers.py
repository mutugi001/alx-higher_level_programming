#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for i in my_list:
        if i is int:
            if x <= length:
                try:
                    print("{:d}".format(i))
                    length = length + 1
                except IndexError:
                    print("IndexError: list index out of range")
    print("\n")
    return(length)
