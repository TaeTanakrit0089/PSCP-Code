'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    first_num = int(input())
    second_num = int(input())
    gcd = euclid([first_num, second_num])
    if gcd == 1:
        print('YES')
    else:
        print('NO')
    print(gcd)


def euclid(num, count=1):
    '''I'll fight for you Albuquerque!'''
    num.sort()
    while num[0] != 0 and num[1] != 0:
        count += 1
        if count % 2 == 0:
            num[1] = num[1] % num[0]
        else:
            num[0] = num[0] % num[1]
    return max(num)


better_call_saul()
