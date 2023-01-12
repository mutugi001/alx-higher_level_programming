#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    add = 0
    for j in uniq:
        add = add + j
    return(add)
