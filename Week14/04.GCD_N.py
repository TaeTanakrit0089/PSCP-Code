'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    all_num = [int(input()) for i in range(int(input()))]
    all_num.sort()
    while len(all_num) > 1:
        temp1, temp2 = all_num[0], all_num[1]
        all_num.pop(0)
        all_num[0] = euclid([temp1, temp2])
    print(*all_num)


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


lwyrup()
