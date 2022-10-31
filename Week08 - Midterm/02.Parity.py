'''Saul Goodman'''

def goodman(word, choice):
    '''Saul Goodman'''
    all_bit = 0
    for i in word:
        if i == '1':
            all_bit += 1

    if all_bit % 2 == 0:
        if choice == 'even':
            word += '0'
        else:
            word += '1'
    else:
        if choice == 'even':
            word += '1'
        else:
            word += '0'
    return word

print(goodman(input(), input().lower()))
