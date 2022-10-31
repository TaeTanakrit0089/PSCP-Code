'''Saul Goodman'''
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

print(euclid([int(input()), int(input())]))

