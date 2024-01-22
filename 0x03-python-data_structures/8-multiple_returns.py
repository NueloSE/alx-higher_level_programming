#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    for idx in sentence:
        count += 1
    if count == 0:
        return (count, None)
    return (count, sentence[0])
