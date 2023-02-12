#!/usr/bin/python3
"""method outside class"""


def inherits_from(obj, a_class):
    """method to check if obj is an instance of a_class"""
    if type(obj) ==  a_class:
        return(False)
    else:
        return(True)
