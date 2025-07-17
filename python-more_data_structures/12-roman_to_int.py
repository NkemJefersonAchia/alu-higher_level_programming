#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(roman_string)):
        if i > 0 and rom[roman_string[i]] > rom[roman_string[i-1]]:
            total += rom[roman_string[i]] - 2 * rom[roman_string[i-1]]
        else:
            total += rom[roman_string[i]]
    return total
