'''Saul Goodman'''

from math import ceil

def main():
    '''Saul Goodman'''
    need_1, need_2, need_3, need_4 = int(input()), int(
        input()), int(input()), int(input())
    lim_1, lim_2, lim_4, lim_3 = int(input()), int(
        input()), int(input()), int(input())

    work1 = ceil(need_1 / lim_1)
    work2 = ceil(need_2 / lim_2)
    work3 = ceil(need_3 / lim_3)
    work4 = ceil(need_4 / lim_4)

    result = find_maax(work1, 0)
    result = find_maax(work2, result)
    result = find_maax(work3, result)
    result = find_maax(work4, result)

    print('%d' % result)


def find_maax(num1, num2):
    '''Saul Goodman'''
    if num1 > num2:
        return num1
    return num2


main()
