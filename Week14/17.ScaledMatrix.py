'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    row, column = int(input()), int(input())
    data = [float(input()) for i in range(row*column)]
    num_min, num_max = min(data), max(data)
    data = [(i + abs(num_min)) for i in data]
    num_min, num_max = min(data), max(data)
    data = [(i/num_max) for i in data]

    count = 0
    for _ in range(row):
        for _ in range(column):
            print('%.02f' % data[count], end=' ')
            count += 1
        print()


lwyrup()
