#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str):
        copy = str
    if str == '\0':
        copy = '\0'
    for i in range(len(str)):
        if str[i] != str[n]:
            copy = copy + str[i]
    return(copy)
