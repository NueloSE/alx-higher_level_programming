#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    divisor = 0
    for tup_score in my_list:
        sum += (tup_score[0] * tup_score[1])
        divisor += tup_score[1]
    return sum / divisor
