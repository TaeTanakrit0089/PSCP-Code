'''Saul Goodman'''


def median():
    '''Saul Goodman'''
    num_per = int(input())
    data = [int(input()) for i in range(num_per)]
    data.sort()
    if num_per % 2 == 0:
        middle = num_per//2 - 1
        result = (data[middle] + data[middle+1]) / 2
    else:
        middle = num_per//2
        result = data[middle]

    print('%.01f' % round(result, 1))


median()
