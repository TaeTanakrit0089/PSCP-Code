"""Python"""


def main():
    """main"""

    num_k = int(input())
    num_n = int(input())
    mid_row = num_n//2 + 1

    space = 0
    for i in range(mid_row):
        print(' '*space, end='')
        print('*'*num_k)
        space += 1
        i = i
    space -= 2
    for i in range(mid_row-1):
        print(' '*space, end='')
        print('*'*num_k)
        space -= 1
        i = i


main()
