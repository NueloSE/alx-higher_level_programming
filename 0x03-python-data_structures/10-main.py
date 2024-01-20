#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

mylist = [0, 1, 2, 3, 4, 5, 6]
result_list = divisible_by_2(mylist)

i = 0
while i < len(result_list):
    print("{:d} {:s} divisible by 2".format(mylist[i], "is" if result_list[i] else "is not"))
    i += 1