'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    summer = 0
    data = [list(map(int, input().split())) for _ in range(int(input()))]
    for i in range(len(data)-1):
        summer += distance(data[i], data[i+1])
    print('%.2f' % summer)


def distance(point_a, point_b):
    '''Saul Goodman'''
    temp = (point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2
    return temp ** 0.5


lwyrup()
