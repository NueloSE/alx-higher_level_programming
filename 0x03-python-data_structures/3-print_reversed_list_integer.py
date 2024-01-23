#!/usr/bin/python3
def _len(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def print_reversed_list_integer(my_list=[]):
    if (my_list == None):
        print()
        exit()
    list_len = _len(my_list) - 1
    while list_len >= 0:
        print("{:d}".format(my_list[list_len]))
        list_len -= 1
