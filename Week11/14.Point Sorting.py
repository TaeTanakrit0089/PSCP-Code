'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    num_t = int(input())
    for _ in range(num_t):
        how_many = int(input())
        data = [input().split() for i in range(how_many)]
        for i in data:
            temp = int(i[0]) + int(i[1])
            i.append(temp)
        data.sort(key=lambda l: l[1], reverse=True)
        data.sort(key=lambda l: l[2])
        for i in data:
            print(i[0], i[1])


better_call_saul()
