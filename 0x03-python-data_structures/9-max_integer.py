#!/usr/bin/python3
def _len(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def max_integer(mylist=[]):
    if _len(mylist) == 0:
        return None
    else:
        max_num = mylist[0]
        for num in mylist:
            if num > max_num:
                max_num = num
    return max_num
