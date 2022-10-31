'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    data = input().split()
    num1 = input()
    num_for_print = data.index(num1)
    all_num = data.count(num1)
    for _ in range(all_num):
        for _ in range(all_num):
            print(num_for_print, end=' ')
        print()

better_call_saul()
