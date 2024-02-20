#!/usr/bin/python3
"""
A module containing a function to divide all elements of a matrix.

The matrix_divided function takes a matrix (list of lists) and a number, and divides all elements
of the matrix by the given number. it returns a new matrix with the elements divided and rounded to 2 decimal places.

Example:
    #Define a matrix
    matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

    #Divide all elements of the matrix by 2
    divided_matrix = matrix_divided(matrix, 2)
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided, must be a list of lists of integer or floats
        div (int or float): The number to divide the elements of the matrix by.

    Raises:
        TypeError: if matrix is not a list of lists of integer or float, or if div is not a number (integer or float).
        ZeroDivisionError: if div is equal to 0.

    Returns:
        list of lists: A new matrix with all elements divided by div, rounded to 2 decimal places.
    """

    if not (isinstance(div, int) | isinstance(div, float)):
        raise TypeError('div must be a number')
    if (div == 0):
        raise ZeroDivisionError("division by zero")
        
    for i in range(len(matrix)):
        if (i + 1)  >= len(matrix):
            break
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    row = len(matrix)    
    col = len(matrix[0])

    divided_matrix = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            element = matrix[i][j]
            if not (isinstance(element, int) | isinstance(element, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            divided_matrix[i][j] = round((element / div), 2)
    
    return divided_matrix
