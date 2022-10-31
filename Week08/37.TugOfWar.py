'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    all_a = 0
    all_b = 0
    for i in range(10):
        all_a += int(input())
        i = i
    for i in range(10):
        all_b += int(input())
        i = i

    if all_a == all_b:
        print('AB')
    elif all_a > all_b:
        print('B')
    elif all_a < all_b:
        print('A')


main()
