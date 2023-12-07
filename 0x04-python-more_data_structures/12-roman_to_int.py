#!/usr/bin/python3
# Check Examples

# python 3.7.1

thousands = ["MMM", "MM", "M"]
hundreds = ["CM", "DCCC", "DCC", "DC", "D",
            "CD", "CCC", "CC", "C"]
tens = ["XC", "LXXX", "LXX", "LX", "L",
        "XL", "XXX", "XX", "X"]
digits = ["IX", "VIII", "VII", "VI", "V",
          "IV", "III", "II", "I"]


def check_digit(string, nums):
    for i in nums:
        if i in string:
            return list(reversed(nums)).index(i) + 1
    return -1


def convert_roman_to_int(string):
    thousand = check_digit(string, thousands)
    if thousand != -1:
        delete = thousands[thousand - 1]
        string = string.replace(delete, '')
    else:
        thousand = 0
    hundred = check_digit(string, hundreds)
    if hundred != -1:
        delete = hundreds[hundred - 1]
        string = string.replace(delete, '')
    else:
        hundred = 0
    ten = check_digit(string, tens)
    if ten != -1:
        delete = tens[ten - 1]
        string = string.replace(delete, '')
    else:
        ten = 0
    digit = check_digit(string, digits)
    if digit != -1:
        delete = digits[digit - 1]
        string = string.replace(delete, '')
    else:
        digit = 0
    return thousand * 1000 + hundred * 100 + ten * 10 + digit


def check_input(string):
    for i in string:
        if i not in 'MCDLXVI':
            return False
    return True


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not check_input(roman_string):
        return 0
    result = convert_roman_to_int(roman_string)
    return result
