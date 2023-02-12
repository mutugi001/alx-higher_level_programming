#!/usr/bin/python3
"""method outside class"""


def lookup(obj):
    """function that returns the list of available attributes
    and methods of a given object"""
    return(dir(obj))
