'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    money, rate, years = int(input()), float(input()), int(input())
    for _ in range(years):
        money *= (100+rate)/100
    print('%.2f' % money)


lwyrup()
