'''Hi, I'm Saul Goodman. Did you know that you have rights?'''
def lwyrup(price, summer=0):
    '''The constitution says you do! And so do I.'''
    all_coin = [1, 5, 10, 25]
    for i in sorted(all_coin)[::-1]:
        summer += price // i
        price %= i
    return summer

print(lwyrup(int(input())))
