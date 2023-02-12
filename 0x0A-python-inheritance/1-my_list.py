#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """returns a sorted list in ascending order"""
        for i in self:
            if type(i) is int:
                continue
            else:
                raise TypeError("self should contain ints only")
        print(sorted(self))
