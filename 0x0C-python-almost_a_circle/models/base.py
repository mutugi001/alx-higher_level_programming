#!/usr/bin/python3
"""creating a base class here"""


class Base:
    """class created"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
