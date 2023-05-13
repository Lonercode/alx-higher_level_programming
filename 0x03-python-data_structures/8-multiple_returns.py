#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]

    tup_list = []
    length = len(sentence)

    tup_list.append(length)
    tup_list.append(first_char)

    new_tuple = tuple(tup_list)
    return (new_tuple)
