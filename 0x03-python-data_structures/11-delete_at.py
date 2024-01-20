#!/usr/bin/python3
def _len(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def delete_at(mylist=[], idx=0):
    list_length = _len(mylist)
    if (idx < 0) | (idx >= list_length):
        return mylist
    i = 0
    while i <= idx:
        if i == idx:
            mylist.remove(mylist[i])
        i += 1
    return mylist
