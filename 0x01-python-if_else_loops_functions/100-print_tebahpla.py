#!/usr/bin/python3
letter = 122
while (letter >= 97):
    count = letter
    if (count % 2) != 0:
        count = count - 32
    print("{}".format(chr(count)), end='')
    letter -= 1
