'''Saul Goodman'''

from math import ceil


def main():
    '''Saul Goodman'''
    temp = int(input())
    for _ in range(temp):
        text_in = input()
        year = int(text_in[5:])
        text_format = text_in[:4]
        if text_format == 'B.E.' and year - 543 >= 0:
            temp = ceil((year-543)/100)
        elif text_format == 'A.D.' and year >= 0:
            temp = ceil(year/100)
        else:
            temp = 'ERROR'
        print(str(temp))


main()
