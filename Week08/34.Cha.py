'''Python'''

from math import ceil


def main():
    '''Python'''
    day = int(input())
    all_hour = 0
    for i in range(day):
        i = i
        hour = float(input())
        all_hour += ceil(hour)

    total = all_hour * 8720
    print(round(total))


main()
