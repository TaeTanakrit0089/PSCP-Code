'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    num1 = float(input())
    if num1 > 14 or num1 < 0:
        print('error')
    elif num1 == 7:
        print('neutral')
    elif num1 >= 0 and num1 < 7:
        print('acidic')
    elif num1 > 7 and num1 <= 14:
        print('akaline')

better_call_saul()
