#!/usr/bin/python3
def common_elements(set_1, set_2):
    newSet = set()
    # return (set_1.intersection(set_2))
    for i in set_2:
        for j in set_1:
            if i == j:
                newSet.add(i)
    return newSet
