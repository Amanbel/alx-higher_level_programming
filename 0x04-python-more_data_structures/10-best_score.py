#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    maxi = 0
    for k in a_dictionary:
        if maxi < a_dictionary[k]:
            maxi = a_dictionary
    for k in a_dictionary:
        if maxi == a_dictionary[k]:
            return k
