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

# clarifications on this line:
# roman_values[roman_string[i]] is the value of the current roman numeral
# roman_values[roman_string[i - 1]] is the value of the previous roman numeral
# roman_values[roman_string[i]] - 2 * roman_values[roman_string[i - 1]]
# is the value of the current roman numeral
# minus twice the value of the previous roman numeral
# this is because the previous roman numeral
# was already added to the result in the previous iteration
# so we need to subtract it twice to get the correct value

# example: roman_string = "IV"
# the first iteration will add 1 to the result
# the second iteration will add 5 to the result
# but we need to subtract 1 twice to get the correct value
# so we subtract 1 twice from 5 to get 3
# and we add 3 to the result

# example: roman_string = "IX"
# the first iteration will add 1 to the result
# the second iteration will add 10 to the result
# but we need to subtract 1 twice to get the correct value
# so we subtract 1 twice from 10 to get 8
# and we add 8 to the result

# example: roman_string = "XL"
# the first iteration will add 10 to the result
# the second iteration will add 50 to the result
# but we need to subtract 10 twice to get the correct value
# so we subtract 10 twice from 50 to get 30
# and we add 30 to the result
