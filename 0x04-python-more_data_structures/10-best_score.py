#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    if a_dictionary == None:
        return max_key
    max_val = next(iter(a_dictionary.values()))
    for key, val in a_dictionary.items():
        if val >= max_val:
            max_val = val
            max_key = key
        
    return max_key
