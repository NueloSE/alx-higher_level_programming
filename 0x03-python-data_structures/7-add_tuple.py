#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    res = ()
    idx = 0

    if (len_a < 2):
        len_a = 2 - len_a
        for i in range(len_a):
            tuple_a += 0,

    if (len_b < 2):
        len_b = 2 - len_b
        for i in range(len_b):
            tuple_b += 0,

    while idx < 2:
        res += ((tuple_a[idx] + tuple_b[idx]), )
        idx += 1

    return (res)
