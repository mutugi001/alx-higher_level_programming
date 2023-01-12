#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return(a_dictionary)
    dict_copy = {}
    for i, j in a_dictionary.items():
        dict_copy[i] = j
    for i, j in dict_copy.items():
        if j == value:
            del(a_dictionary[i])
    return(a_dictionary)
