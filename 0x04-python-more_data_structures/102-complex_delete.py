#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return(a_dictionary)
    for i, j in a_dictionary.item():
        if j == value:
            del(a_dictionary[i])
    return(a_dictionary)
