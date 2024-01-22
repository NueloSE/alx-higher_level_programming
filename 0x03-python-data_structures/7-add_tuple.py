#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    longest_len = (len_a) if (len(tuple_a) > len(tuple_b)) else (len_b)
    for idx in range(longest_len):
        if (idx < len_a) & (idx < len_b):
            res += (tuple_a[idx] + tuple_b[idx]),
        elif idx >= len_a:
            res += (tuple_b[idx]),
        elif idx >= len_b:
            res += (tuple_a[idx]),
    return res
