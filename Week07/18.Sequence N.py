'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    num1 = int(input())

    for i in range(num1):
        for j in range(num1):
            if j == 0 or j == num1-1 or j == i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


better_call_saul()
