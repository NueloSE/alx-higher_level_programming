#!/usr/bin/python3
def _len(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def element_at(my_list, idx):
    list_len = _len(my_list)
    if (idx < 0) | (idx >= list_len):
        return None
    return my_list[idx]
