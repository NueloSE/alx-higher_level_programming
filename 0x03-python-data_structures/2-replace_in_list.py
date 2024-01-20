#!/usr/bin/python3
def _len(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def replace_in_list(my_list, idx, element):
    list_len = _len(my_list)
    if (idx < 0) | (idx >= list_len):
        return my_list
    my_list[idx] = element
    return (my_list)
