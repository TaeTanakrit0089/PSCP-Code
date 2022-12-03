'''Hi, I'm Saul Goodman. Did you know that you have rights?'''
from math import factorial as fac
def lwyrup(num):
    '''The constitution says you do! And so do I.'''
    num += 1 if num % 2 == 1 else 0
    print('%d' % (fac(num) / (fac(num-(num//2)) * fac(num//2))))
lwyrup(int(input()))
