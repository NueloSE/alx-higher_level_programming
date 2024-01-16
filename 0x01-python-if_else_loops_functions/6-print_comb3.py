#!/usr/bin/python3
digit1 = 48
while digit1 <= 56:
    digit2 = digit1 + 1
    while digit2 <= 57:
        if (digit1 == 56) & (digit2 == 57):
            print("{}{}".format(chr(digit1), chr(digit2)))
        else:
            print("{}{}, ".format(chr(digit1), chr(digit2)), end='')
        digit2 += 1
    digit1 += 1
