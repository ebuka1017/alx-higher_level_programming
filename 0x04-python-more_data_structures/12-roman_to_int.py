#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string  is None or not isinstance(roman_string, str):
        return ("0")
    
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    lst = 0
    tot = 0

    for numeral in reversed(roman_string):
        val = numerals.get(numeral, 0)
        if (val >= lst):
            tot += val
        else:
            tot -= val
            lst = val
    return tot
