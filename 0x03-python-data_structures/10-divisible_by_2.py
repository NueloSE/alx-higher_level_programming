#!/usr/bin/python3
def _len(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def divisible_by_2(mylist=[]):
    if _len(mylist) == 0:
        return mylist
    else:
        result = []
        for num in mylist:
            if num % 2 == 0:
                result.append(True)
            else:
                result.append(False)
    return result
