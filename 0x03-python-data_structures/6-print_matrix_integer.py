#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if num == 3 or num == 6 or num == 9:
                print("{:d}".format(num), end="")
            else:
                 print("{:d}".format(num), end=" ")

        print("")
