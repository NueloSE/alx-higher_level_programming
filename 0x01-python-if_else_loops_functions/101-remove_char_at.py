#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    for i in str:
        if n == 0:
            strcpy += ''
        else:
            strcpy += i
        n -= 1
    return (strcpy)
