#!/usr/bin/python3
def best_score(a_dictionary):
    largest = 0
    name = ""
    if a_dictionary is None:
        return(None)
    for i, j in a_dictionary.items():
        if j > largest:
            largest = j
    for i, j in a_dictionary.items():
        if j == largest:
            return(i)
