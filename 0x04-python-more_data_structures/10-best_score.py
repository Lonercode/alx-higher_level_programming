#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return (None)
    else:
        max = list(a_dictionary.values())[0]
        for i in a_dictionary.values():
            if i > max:
                max = i
        return (max)