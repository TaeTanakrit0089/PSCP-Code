'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    num = int(input())
    if num % 3 == 0 or str(num)[-1] == '3':
        print('PONG')
    else:
        print(num)

lwyrup()
