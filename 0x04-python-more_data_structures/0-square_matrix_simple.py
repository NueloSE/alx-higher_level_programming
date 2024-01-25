#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    numRow = len(matrix)
    if (numRow == 0):
        return []

    numCol = len(matrix[0])

    matrixDouble = [[0] * numCol for i in range(numRow)]

    for i in range(numRow):
        for j in range(numCol):
            matrixDouble[i][j] = (matrix[i][j] ** 2)

    return (matrixDouble)
