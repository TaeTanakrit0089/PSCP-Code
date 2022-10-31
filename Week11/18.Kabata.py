'''Saul Goodman'''
def better_call_saul(num1):
    '''I'll fight for you Albuquerque!'''
    for _ in range(num1):
        word = input()
        all_possible = ['bakka', 'ka', 'ba', 'ta']
        restrict_word = ['baka']
        for i in restrict_word:
            word = word.replace(i, 'SaulGoodman')
        for i in all_possible:
            word = word.replace(i, '')
        if word == '':
            print('yes')
        else:
            print('no')
better_call_saul(int(input()))
