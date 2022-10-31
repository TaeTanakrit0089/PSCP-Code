'''Saul Goodman'''


def huell():
    '''Saul Goodman'''
    punch_time = int(input())
    punch_set = int(input())
    punch_all, last_run = 0, 0
    for i in range(2, punch_time+1, 2):
        last_run = i
        if punch_all >= punch_set:
            punch_all += 12 * (punch_time - last_run + 1)
            break

        if i % 6 == 0:
            punch_all += 1
        elif i % 2 == 0:
            punch_all += 165
    print(punch_all)


huell()
