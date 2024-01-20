#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_num = len(matrix)
    col_num = len(matrix[0])

    for rowIdx in range(row_num):
        for colIdx in range(col_num):
            print("{:d}".format(matrix[rowIdx][colIdx]), end="")
            if colIdx == col_num - 1:
                break
            else:
                print(" ", end='')
        print()
