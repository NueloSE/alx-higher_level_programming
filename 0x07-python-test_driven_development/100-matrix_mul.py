#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    if not (type(m_a) is list):
        raise TypeError('m_a must be a list')
    if not (type(m_b) is list):
        raise TypeError('m_b must be a list')
    if not (type(m_a[0]) is list):
        raise TypeError('m_a must be a list of lists')
    if not (type(m_b[0]) is list):
        raise TypeError('m_b must be a list of lists')
    if (len(m_a) == 0) | (len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if (len(m_b) == 0) | (len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            if not (isinstance(m_a[i][j], int) | isinstance(m_a[i][j], float)):
                raise TypeError("m_a should contain only integers or floats")

    for i in range(len(m_b)):
        for j in range(len(m_b[i])):
            if not (isinstance(m_b[i][j], int) | isinstance(m_b[i][j], float)):
                raise TypeError("m_b should contain only integers or floats")

    m_a_row = len(m_a)
    m_b_row = len(m_b)

    m_a_col = len(m_a[0])
    for i in range(m_a_row):
        if len(m_a[i]) != m_a_col:
            raise TypeError('each row of m_a must be of the same size')

    m_b_col = len(m_b[0])
    for i in range(m_b_row):
        if len(m_b[i]) != m_b_col:
            raise TypeError("each row of m_b must be of the same size")

    if (m_a_col != m_b_row):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[0] * m_b_col for i in range(m_a_row)]

    for i in range(m_a_row):
        for j in range(m_b_col):
            k = 0
            c_i = m_a[i][k] * m_b[k][j]
            k = 1
            c_j = m_a[i][k] * m_b[k][j]

            m_c[i][j] = c_i + c_j
    return m_c
