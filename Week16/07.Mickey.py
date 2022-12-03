'''Saul Goodman'''


def better_call_saul(rat_num):
    '''Saul Goodman'''
    rat = sorted([float(input()) for i in range(rat_num)])
    houses = sorted([float(input()) for i in range(rat_num)])
    data = sorted([abs(rat[i]-houses[i]) for i in range(rat_num)])
    print(int(data[-1]))


better_call_saul(int(input()))
