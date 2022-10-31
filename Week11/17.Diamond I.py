'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    num_m = int(input())
    num_n = int(input())
    data = [input().split() for i in range(num_m)]
    sum_row = []
    for i in range(num_n):
        temp = 0
        for j in data:
            temp += int(j[i])
        sum_row.append(temp)
    print(max(sum_row))


better_call_saul()
