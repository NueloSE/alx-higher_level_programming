#!/usr/bin/python3
def _len(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def new_in_list(my_list, idx, element):
    length = _len(my_list)
    if (idx < 0) | (idx > length):
        return (my_list)
    list_cpy = []
    for num in my_list:
        list_cpy.append(num)
    list_cpy[idx] = element
    return list_cpy
