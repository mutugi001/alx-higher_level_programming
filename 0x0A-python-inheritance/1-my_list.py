#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """returns a sorted list in ascending order"""

        print(sorted(self))
