#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str):
        copy = str
    if str == '\0':
        copy = '\0'
    for i in str:
        if i != str[n]:
            copy = i
    return(copy)
