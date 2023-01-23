#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 1
    elements = 0
    for i in my_list:
        if x >= length:
            try:
                print("{}".format(i),end='')
                if i != '\0' :
                    elements = elements + 1
            except IndexError:
                print("index is not available")
        length = length + 1
    print("\n")
    return (elements)
