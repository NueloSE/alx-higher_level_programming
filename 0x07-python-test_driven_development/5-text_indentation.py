#!/usr/bin/python3

"""
This module contains a function that takes a text as an argument
It prints it to the stdout in a formatted format
"""


def text_indentation(text):
    """
    ``text_indentation`` function prints a text argument passed to the
    stdout by print 2 new lines after these charactes: '.', '?' and ':'
    """
    err = "text_indentation() missing 1 required positional argument: 'text'"
    if text == '':
        raise TypeError(err)
    if not (isinstance(text, str)):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        word = text[i]
        if ((text[i - 1] in ['.', '?', ':']) and (word.startswith(' '))):
            word = word[1:]
        if (word == '.') | (word == '?') | (word == ':'):
            print('{}\n'.format(word))
        else:
            print(word, end='')
