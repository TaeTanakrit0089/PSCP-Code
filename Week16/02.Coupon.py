'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    price, coupon1, coupon2 = float(input()), list(
        map(float, input().split())), list(map(float, input().split()))
    chance1 = price - coupon1[0] if price > coupon1[1] else price
    chance2 = price - (coupon2[0]/100*price) if price > coupon2[1] else price
    if min(chance1, chance2) == price:
        print('Nope')
    else:
        print(1 if chance1 < chance2 else 2, '%.1f' % min(chance1, chance2))
better_call_saul()
