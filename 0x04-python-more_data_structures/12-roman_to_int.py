#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return (0)
    else:
        dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
        val = 0
        for i in range(len(roman_string)):
            if i > 0 and dict1[roman_string[i]] > dict1[roman_string[i - 1]]:
                val += dict1[roman_string[i]] - 2 * dict1[roman_string[i - 1]]
            else:
                val += dict1[roman_string[i]]
        return (val)
