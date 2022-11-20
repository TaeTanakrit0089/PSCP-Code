'''Saul Goodman'''


def huell():
    '''Saul Goodman'''
    isbn = input().replace(' ', '').replace('-', '').replace('X', '55')
    temp, summer = 10, 0
    for i in isbn[:-1]:
        summer += int(i) * temp
        temp -= 1
    summer *= -1

    if summer % 11 == int(isbn[-1]):
        print('Yes')
    else:
        if summer % 11 < 10:
            result = summer % 11
        else:
            result = 'X'
        print('No', result)


huell()
