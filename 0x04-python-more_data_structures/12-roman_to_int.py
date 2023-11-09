#!/usr/bin/python3

def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer."""
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_values[roman_string[i]] > roman_values[roman_string[i - 1]]:
            result += roman_values[roman_string[i]] - 2 * roman_values[roman_string[i - 1]]
        else:
            result += roman_values[roman_string[i]]
    return result
