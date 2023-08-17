#!/usr/bin/python3

import roman

def roman_to_int(roman_string):
    if roman_string  is None or not isinstance(roman_string, str):
        return ("0")
    else:
        return roman.fromRoman(roman_string)
