'''Saul Goodman'''

from math import ceil


def main():
    '''Saul Goodman'''
    num_n, num_k, num_x, num_y = int(input()), int(
        input()), int(input()), int(input())
    day_count, page_read, count = 0, 0, 0
    while True:
        temp = ceil(num_x/num_y*num_k)
        condi1 = num_n == count
        condi2 = temp >= num_k
        if condi1 or condi2:
            day_count += num_n-count
            break
        page_read += temp
        if page_read >= num_k:
            count += 1
            page_read = 0
        num_x += 1
        num_y += 1
        day_count += 1

    print(day_count)


main()
