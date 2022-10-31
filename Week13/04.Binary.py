'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def decimal_to_biinary(decimal, biinary=''):
    '''The Constitution says you do, and so do I.'''
    if decimal == 0:
        return decimal
    while decimal:
        biinary += str(decimal % 2)
        decimal = decimal // 2
    return biinary[::-1]

print(decimal_to_biinary(int(input())))
