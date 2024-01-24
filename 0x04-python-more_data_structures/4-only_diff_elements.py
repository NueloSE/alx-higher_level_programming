#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # newSet = set()
    # for i in set_1:
    #     for j in set_2:
    #         if j == i:
    #             continue
    #         newSet.add(j)
    # return newSet

    return set_1.symmetric_difference(set_2)
