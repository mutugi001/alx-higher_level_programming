#!/usr/bin/python3
"""defining a class square"""
class Square:
    """initializing class square"""
    def __init__(self, size=0):
        """args: size, size of square"""
        self.__size = size

    @property
    def size(self):
        """getter for attribute size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """setter for size attribute"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """finding area of the square"""
        area = self.__size * self.__size
        return(area)

    def my_print(self):
        """prints in stdout the square with the character #"""
        i = 0
        j = 0
        if self.__size == 0:
            print("\n")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
                j = j + 1
            print("\n", end='')
            i = i + 1
