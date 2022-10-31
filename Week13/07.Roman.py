'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    num_replace = {'IV': 'A', 'IX': 'B',
                   'XL': 'E', 'XC': 'F', 'CD': 'G', 'CM': 'H'}
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
             'M': 1000, 'A': 4, 'B': 9, 'E': 40, 'F': 90, 'G': 400, 'H': 900}

    roman_num, result = input(), 0
    for key, values in num_replace.items():
        roman_num = roman_num.replace(key, values)
    for i in roman_num:
        result += roman[i]
    print(result)


better_call_saul()
