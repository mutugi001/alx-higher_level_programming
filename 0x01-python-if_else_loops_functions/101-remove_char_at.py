#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    if len(str) == n:
        copy = str
        return(copy)
    if n < 0:
        copy = str
        return(copy)
    if str == '\0':
        copy = '\0'
    for i in range(len(str)):
        if str[i] != str[n]:
            copy = copy + str[i]
    return(copy)
